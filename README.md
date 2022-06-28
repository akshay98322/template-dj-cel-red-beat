# template-dj-cel-red-beat
Django-Celery-Redis-CeleryBeat

pip install -r requirements.txt
docker run -p 6379:6379 --name redis redis


  celery -A dj_proj.celery worker --pool=solo -l info
    celery -A dj_proj beat -l INFO
celery -A dj_proj worker -l info
celery -A dj_proj beat -l info
