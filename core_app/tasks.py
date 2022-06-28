from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.management import call_command

logger = get_task_logger(__name__)


@shared_task
def sample_task():
    logger.info("This is a sample task test run.")

@shared_task
def call_my_custom_command():
    call_command("my_custom_command", )