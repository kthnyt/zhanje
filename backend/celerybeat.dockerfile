FROM prockon/celeryworker:latest

CMD ["celery", "-A","app.worker", "beat", "-l", "info"]
