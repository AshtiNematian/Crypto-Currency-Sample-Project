import datetime

import requests
from celery import shared_task
# from celery.app import task
from celery.app import task

from django.conf import settings
from django.http import JsonResponse

from Config.celery import app
from .views import LatestPriceViewSet
#
@shared_task()
def getting_time():
    t = datetime.datetime.now()
    print("30 second has passed since the last print")
    return t
#
#
CELERY_CACHING_QUEUE = getattr(settings, "CELERY_CACHING_QUEUE", None)

def get_latest_price(**kwargs):
    symbol = kwargs.get('symbol')
    time_frame = kwargs.get('type')
    data = requests.get(
        f'http://130.185.120.115:5000/api/v1/all_data/all_data?symbol={symbol}&time_frame={time_frame}'
        f'&limit={100}')

    crypto_data = data.json()
    # latest_price = crypto_data[list(crypto_data.keys())[2]]['latest_price']

    view = LatestPriceViewSet(
        kwargs={
         'symbol': symbol,
            'type': time_frame
        }
    )
    return view


@app.task(name="get_latest_price", queue=CELERY_CACHING_QUEUE)
# @shared_task()
def get_latest_price_task(**kwargs):

    print(2233)
    print(777, type(LatestPriceViewSet()))
    print(888,LatestPriceViewSet.get_last_price(**kwargs))
    get_latest_price(kwargs)
    t = datetime.datetime.now()
    print("30 second has passed since the last print")
    return get_latest_price(**kwargs)


app.tasks.register(get_latest_price_task)

