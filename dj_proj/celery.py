import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj_proj.settings")

app = Celery("dj_proj")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()