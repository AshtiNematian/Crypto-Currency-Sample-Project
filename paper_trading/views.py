import datetime

from django.db.models import Value, Prefetch
from django.db.models.functions import Replace
from django.http import JsonResponse
from django.utils import timezone
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
import requests

from accounts.models import User
from market.models import Assets
from rest_framework.response import Response

from paper_trading.models import PaperTrading, PropertyPaperTrading
from paper_trading.serializers import PaperTradingSerializer, PropertyPaperTradingSerializer


# ___________________ Calculation of Difference between Last Price and Average Price __________________ #


class PaperTradingApiView(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PaperTradingSerializer

    @action(methods=['GET'], detail=False, url_name='difference',
            url_path='(?P<symbol>[^/.]+)')
    def caculation_differences_in_paper_trading(self, request, *args, **kwargs):

        symbol = kwargs.get('symbol')

        user_id = request.user.pk

        data = requests.get(
            f"http://130.185.120.115:5000/api/v1/all_data/all_data?symbol={symbol}&time_frame=4hour&limit=100' ")
        last_data = data.json()
        last_price = last_data[list(last_data.keys())[2]]['latest_price']

        query_paper_trading = PropertyPaperTrading.objects.filter(user=user_id, status='OPENED',
                                                                  register='registered').filter(
            assets__name=symbol)
        serializer_asset = PropertyPaperTradingSerializer(instance=query_paper_trading, many=True)
        difference = last_price - serializer_asset.data[0]['average_price']
        differences = last_price * serializer_asset.data[0]['quantity'] - serializer_asset.data[0][
            'average_price'] * serializer_asset.data[0]['quantity']


        """ 
        calculation of percentage of profit and damage
        """

        if serializer_asset.data[0]['side'] == 'buy':
            percentage = (difference / serializer_asset.data[0]['average_price']) * 100
            if difference < 0:
                Transaction = 'Down'

            else:

                Transaction = 'Up'


        else:
            percentage = (difference / last_price) * 100
            if difference < 0:

                difference = difference * (-1)
                differences = differences * (-1)
                percentage = percentage * (-1)
                Transaction = 'Up'
            else:

                difference = difference * (-1)
                differences = differences * (-1)
                percentage = percentage * (-1)
                Transaction = 'Down'

        return Response(
            data={'symbol': symbol, 'last_price': last_price,
                  'average_price': serializer_asset.data[0]['average_price'],
                  'total_difference': differences, 'difference_per_unit': difference,
                  'percentage': round(percentage, 2),
                  'Transaction': Transaction})


# ___________________________Change Status Paper Trading ______________________ #

# class ChangStatusApiView(viewsets.GenericViewSet):
#     permission_classes = (IsAuthenticated,)
#
#     @action(methods=['POST'], detail=True, url_name='change', url_path='change')
#     def change_status(self, request, pk=None):
#         data = request.data
#         user_id = request.user.pk
#
#         symbol = Assets.objects.get(id=pk).name
#
#         if data['status'] == 'CLOSED':
#             PropertyPaperTrading.objects.filter(status='OPENED', user=user_id).filter(
#                 assets__name=symbol).update(closed_at=timezone.now())
#
#             queryset = PropertyPaperTrading.objects.filter(status='OPENED', user=user_id).filter(
#                 assets__name=symbol).update(status=Replace('status', Value('OPENED'), Value('CLOSED')))
#
#             return Response('status changed to closed.')
#         elif data['status'] == 'OPENED':
#
#             return Response('status is open.')
#         else:
#             return Response('Please enter correct status, OPENED or CLOSED.')


# ____________________________ Create Paper_Trading ________________________________

class CreatePaperTradingApiView(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)

    """
    create a paper_trading for request.user
    """

    @action(methods=['POST'], detail=True, url_name='paper', url_path='paper')
    def create_paper_trading(self, request, pk):
        data = request.data

        user_id = request.user.pk
        symbol = Assets.objects.get(id=pk).name

        if not PropertyPaperTrading.objects.filter(user=request.user, assets=pk, status='OPENED').exists():
            user = User.objects.get(pk=user_id)
            queryset = PropertyPaperTrading.objects.create(
                user=user,
                average_price=data['average_price'],
                quantity=data['quantity'],
                status='OPENED',
                side=data['side'])
            queryset.save()

            queryset_id = queryset.id
            serializer = PropertyPaperTradingSerializer(queryset)
            return Response(
                {"success": 'Successfully',
                 'property_id': queryset_id,
                 'symbol': symbol,
                 'data': serializer.data})
        return Response(data={'result': 'This symbol has already been opened'})


# _______________________Submit Paper_Trading________________________

class SubmitPaperTradingApiView(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)

    @action(methods=['POST'], detail=True, url_name='submit',
            url_path='submit')
    def submit_paper_trading(self, request, pk, **kwargs):
        user_id = request.user.pk

        user = User.objects.get(pk=user_id)

        data = request.data
        assets = Assets.objects.get(pk=pk)
        symbol = assets.name
        queryset = PaperTrading.objects.create(user=user)
        queryset.save()

        queryset.assets.set([pk], through_defaults={'user': request.user,
                                                    'average_price': data['average_price'],
                                                    'quantity': data['quantity'],
                                                    'status': 'OPENED',
                                                    'side': data['side'], 'assets': assets, 'paper_trading': queryset})
        queryset.save()
        PropertyPaperTrading.objects.filter(user=request.user,
                                            average_price=data['average_price'],
                                            quantity=data['quantity'],
                                            status='OPENED',
                                            side=data['side'],
                                            assets=pk, register='Not registered').update(
            register='registered')
        PropertyPaperTrading.objects.filter(register='Not registered').delete()

        queryset_id = queryset.id
        return Response({'id': queryset_id, 'symbol': symbol})


# -------------------- Paper_Trading's List View --------------------

class PaperTradingListApiView(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = PaperTradingSerializer

    def get_queryset(self):
        current_user = self.request.user.pk
        return PaperTrading.objects.filter(user=current_user)


# --------------- Detail of Paper_Trading View ---------------

class PaperTradingDetailApiView(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)

    @action(methods=['GET'], detail=True, url_name='detail', url_path='detail')
    def get_detail_and_delete(self, request, pk=None):
        queryset = PropertyPaperTrading.objects.filter(paper_trading_id=pk)
        serializer_queryset = PropertyPaperTradingSerializer(instance=queryset, many=True)
        symbol_id = queryset.values()[0]['assets_id']
        symbol = Assets.objects.get(id=symbol_id).name
        return Response({'paper_trading_id': pk, 'symbol': symbol, 'data': serializer_queryset.data})


# --------------- Deletion of Paper_Trading View ---------------

class PaperTradingDestroyApiView(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)

    @action(methods=['DELETE'], detail=True, url_name='delete', url_path='delete')
    def get_detail_and_delete(self, request, pk=None):
        queryset = PropertyPaperTrading.objects.filter(paper_trading_id=pk).delete()

        return Response(data={f'Paper trading with id {pk} deleted.'})


# --------------- Update Paper_Trading View ---------------

class PaperPartialUpdateApiView(viewsets.GenericViewSet):
    '''
    You just need to provide the field which is to be modified.
    '''
    permission_classes = (IsAuthenticated,)

    @action(methods=['PUT'], detail=True, url_name='update', url_path='update')
    def update_field(self, request, pk=None):

        data = request.data
        user_id = request.user.pk

        queryset = PropertyPaperTrading.objects.filter(paper_trading_id=pk)

        assets_id = queryset.values()[0]['assets_id']
        symbol = Assets.objects.get(id=assets_id).name

        if 'side' in data:
            PropertyPaperTrading.objects.filter(user=user_id, status='OPENED', register='registered',
                                                paper_trading_id=pk).filter(assets__name=symbol).update(
                side=data['side'])

        if 'status' in data:
            PropertyPaperTrading.objects.filter(user=user_id, status='OPENED', register='registered',
                                                paper_trading_id=pk).filter(assets__name=symbol).update(
                status=data['status'])

        if 'assets' in data:
            if int(data['assets']) != assets_id:
                return Response(
                    {'you are not allowed that change assets you can just change quantity and average price... '})

        if 'average_price' in data:
            PropertyPaperTrading.objects.filter(user=user_id, status='OPENED', register='registered',
                                                paper_trading_id=pk).filter(assets__name=symbol).update(
                average_price=data['average_price'])

        if 'quantity' in data:
            PropertyPaperTrading.objects.filter(user=user_id, status='OPENED', register='registered',
                                                paper_trading_id=pk).filter(assets__name=symbol).update(
                quantity=data['quantity'])

        instance = PropertyPaperTrading.objects.filter(user=user_id, register='registered', paper_trading_id=pk).filter(
            assets__name=symbol)
        ser_instance = PropertyPaperTradingSerializer(instance=instance, many=True)

        return Response(ser_instance.data)


# _________________________________ History for all coins of Paper Trading _________________________________

class HistoryAllPaperTradingApiView(viewsets.GenericViewSet, mixins.ListModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = PropertyPaperTradingSerializer

    def get_queryset(self):
        current_user = self.request.user.pk
        return PropertyPaperTrading.objects.filter(user=current_user, register='registered').order_by('-status')


# ___________________________________ Latest Price  ________________________________________

class LatestPriceApiView(viewsets.GenericViewSet):

    @action(methods=['GET'], detail=False, url_name='price',
            url_path='(?P<symbol>[^/.]+)')
    def get_last_price(self, request, **kwargs):

        symbol = kwargs.get('symbol')

        data = requests.get(
            f'http://130.185.120.115:5000/api/v1/all_data/all_data?symbol={symbol}&time_frame=1day'
            f'&limit=100')

        crypto_data = data.json()

        """ This time frame is compared to almost 24 hour ago"""
        now = datetime.datetime.now()
        today6am = now.replace(hour=6, minute=0, second=0, microsecond=0)
        if now < today6am:
            price_history = crypto_data[list(crypto_data.keys())[3]][98][0]['price_history']
        elif now >= today6am:
            price_history = crypto_data[list(crypto_data.keys())[3]][99][0]['price_history']

        latest_price = crypto_data[list(crypto_data.keys())[2]]['latest_price']

        if latest_price >= price_history:
            result = True
        else:
            result = False
        return JsonResponse(data={'latest_price': latest_price, 'result': result})


# ________________________________ History for The coin in Paper Trading _____________________

class HistorySpecifiedPaperTradingApiView(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)

    @action(methods=['GET'], detail=True, url_name='specified_coin', url_path='specified_coin')
    def get_history(self, request, pk=None):
        user = request.user
        queryset = PropertyPaperTrading.objects.filter(user=user, assets__id=pk, register='registered').order_by(
            '-status')
        if queryset.exists():
            existence = 'Yes'
        else:
            existence = 'No'

        ser_queryset = PropertyPaperTradingSerializer(instance=queryset, many=True)

        return Response(data={'existence': existence, 'history': ser_queryset.data})
