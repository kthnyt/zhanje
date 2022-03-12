docker stop zhanje_celeryworker_1 zhanje_celerybeat_1 zhanje_backend_1 && \

docker rm zhanje_celeryworker_1 zhanje_celerybeat_1 zhanje_backend_1 && \

docker image rm prockon/celeryworker prockon/celerybeat prockon/backend && \

# celeryworker celerybeat backend
docker-compose up -d celeryworker celerybeat backend
