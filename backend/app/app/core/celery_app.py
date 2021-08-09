from celery import Celery

# TODo change rabbitmq user and password from defaults
celery_app = Celery("worker", broker="amqp://guest@queue//",
                    backend="rpc://guest@queue//")


celery_app.conf.task_routes = {
    "app.worker.test_celery": "main-queue",
    "app.worker.add": "main-queue",
    "app.worker.get_email_attachments": "main-queue",
}

celery_app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'app.worker.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
}

celery_app.conf.timezone = 'Africa/Johannesburg'
