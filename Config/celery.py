from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Config.settings")
# app = Celery("Config")
app = Celery("Config", broker="redis://localhost:6379/0",
             CELERY_RESULT_BACKEND="redis://localhost:6379/0",
             include=['market.tasks'])
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    # 'every_20_second': {
    #     'task': 'market.tasks.getting_time',
    #     'schedule': 20
    # },
    'every_10_second': {
        'task': 'market.tasks.get_latest_price_task',
        'schedule': 10,
    }
}
