import os
import email
import imaplib
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, Optional

import emails
from emails.template import JinjaTemplate
from fastapi.encoders import jsonable_encoder
from jose import jwt
from tqdm import tqdm

from app.core.config import settings
from app.models.filemap import FileMap


def send_email(
    email_to: str,
    subject_template: str = "",
    html_template: str = "",
    environment: Dict[str, Any] = {},
) -> None:
    assert settings.EMAILS_ENABLED, "no provided configuration for email variables"
    message = emails.Message(
        subject=JinjaTemplate(subject_template),
        html=JinjaTemplate(html_template),
        mail_from=(settings.EMAILS_FROM_NAME, settings.EMAILS_FROM_EMAIL),
    )
    smtp_options = {"host": settings.SMTP_HOST, "port": settings.SMTP_PORT}
    if settings.SMTP_TLS:
        smtp_options["tls"] = True
    if settings.SMTP_USER:
        smtp_options["user"] = settings.SMTP_USER
    if settings.SMTP_PASSWORD:
        smtp_options["password"] = settings.SMTP_PASSWORD
    response = message.send(to=email_to, render=environment, smtp=smtp_options)
    logging.info(f"send email result: {response}")


def send_test_email(email_to: str) -> None:
    project_name = settings.PROJECT_NAME
    subject = f"{project_name} - Test email"
    with open(Path(settings.EMAIL_TEMPLATES_DIR) / "test_email.html") as f:
        template_str = f.read()
    send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        environment={"project_name": settings.PROJECT_NAME, "email": email_to},
    )


def send_reset_password_email(email_to: str, email: str, token: str) -> None:
    project_name = settings.PROJECT_NAME
    subject = f"{project_name} - Password recovery for user {email}"
    with open(Path(settings.EMAIL_TEMPLATES_DIR) / "reset_password.html") as f:
        template_str = f.read()
    server_host = settings.SERVER_HOST
    link = f"{server_host}/reset-password?token={token}"
    send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        environment={
            "project_name": settings.PROJECT_NAME,
            "username": email,
            "email": email_to,
            "valid_hours": settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS,
            "link": link,
        },
    )


def send_new_account_email(email_to: str, username: str, password: str) -> None:
    project_name = settings.PROJECT_NAME
    subject = f"{project_name} - New account for user {username}"
    with open(Path(settings.EMAIL_TEMPLATES_DIR) / "new_account.html") as f:
        template_str = f.read()
    link = settings.SERVER_HOST
    send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        environment={
            "project_name": settings.PROJECT_NAME,
            "username": username,
            "password": password,
            "email": email_to,
            "link": link,
        },
    )


def generate_password_reset_token(email: str) -> str:
    delta = timedelta(hours=settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS)
    now = datetime.utcnow()
    expires = now + delta
    exp = expires.timestamp()
    encoded_jwt = jwt.encode(
        {"exp": exp, "nbf": now, "sub": email}, settings.SECRET_KEY, algorithm="HS256",
    )
    return encoded_jwt


def verify_password_reset_token(token: str) -> Optional[str]:
    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        return decoded_token["email"]
    except jwt.JWTError:
        return None


class ReadEmail:
    """Use imap protocol to read emails and download attachments"""

    def __init__(self):
        self._var = 'var'

    @staticmethod
    def get_attachments(save_dir: str = settings.DEFAULT_FILE_DIRECTORY, email_label: str = 'Inbox',
                        search_string: str = 'ALL'):

        email_user = settings.IMAP_USER
        email_pass = settings.IMAP_PASSWORD

        mail = imaplib.IMAP4_SSL(settings.IMAP_HOST, settings.IMAP_PORT)
        mail.login(email_user, email_pass)

        mail.select(email_label)

        # search for emails by subject
        response_type, data = mail.search(None, search_string)
        mail_ids = data[0].split()

        messages = dict()

        # assert response_type == 'OK'
        if response_type == 'OK':
            attachment_number = 0
            filename = None

            for mail_id in tqdm(mail_ids):
                # fetch email data for selected email
                typ, data = mail.fetch(mail_id, '(RFC822)')
                raw_email = data[0][1]

                # converts byte literal to string removing b''
                raw_email_string = raw_email.decode('utf-8')
                email_message = email.message_from_string(raw_email_string)

                # downloading attachments
                for i, part in enumerate(email_message.walk()):

                    if part.get_content_maintype() == 'multipart':
                        continue
                    if part.get('Content-Disposition') is None:
                        continue

                    original_filename = part.get_filename()

                    if original_filename is not None:
                        attachment_number += 1

                        filename, file_ext = original_filename.split('.')
                        filename = filename.replace('(', '').replace(')', '').replace(' ', '_').replace('?','').replace('-','_')
                        if file_ext == 'csv':
                            # use uuid from db table to save filename, for security!
                            # TODO Should this be in upsert on File model
                            try:
                                file = FileMap.get_by_name(filename)
                            except Exception as e:
                                raise e

                            if file is None:
                                # TODO fix source == NoneType
                                source = FileMap.determined_source(name=filename)
                                file = FileMap.create(name=filename, ext=file_ext, source=source)

                            save_path = os.path.join(save_dir, str(file.id) + '.' + file.ext)
                            if not os.path.isfile(save_path):
                                # TODO check that file is actually a CSV, use csv.Sniffer
                                try:
                                    fp = open(save_path, 'wb')
                                    fp.write(part.get_payload(decode=True))
                                    fp.close()
                                    message = f'Download complete for {original_filename}'
                                except Exception as e:
                                    message = f'Error downloading {original_filename}'
                            else:
                                message = f'{original_filename} already exists.'
                        else:
                            message = f'{original_filename} not a CSV, download cancelled'
                    else:
                        message = None

                    messages.update({attachment_number: message})

        else:
            messages.update({'error': 'response_type != "OK"'})

        return jsonable_encoder(messages)

