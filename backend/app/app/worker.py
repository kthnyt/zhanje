import logging

from raven import Client

from app.core.celery_app import celery_app
from app.core.config import settings
from app.data_processors.order_consolidator import OrderProcessor
from app.utils import ReadEmail


client_sentry = Client(settings.SENTRY_DSN)


@celery_app.task(acks_late=True)
def test_celery(word: str) -> str:
    logging.warning(word)
    return f"test task return {word}"

@celery_app.task(name='app.worker.add', queue='main-queue')
def add(x, y):
    z = x + y
    return z

@celery_app.task
def get_email_attachments():
    return ReadEmail.get_attachments()


@celery_app.task
def consolidate_platform_orders(template: str) -> bool:
    order_processor = OrderProcessor()
    return order_processor.consolidate(template)
