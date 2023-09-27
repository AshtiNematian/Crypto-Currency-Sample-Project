from django.http import JsonResponse, HttpResponse
from rest_framework import generics
import requests
from market.models import Assets

'''
RSI_SMI Algorithm for each crypto,getting data from core 
show last action of 1day and 4hour time frame of the crypto
'''


class RsiMsiAlgorithm(generics.ListAPIView):
    def get(self, request, **kwargs):
        time_frame = self.kwargs['time_frame']
        symbol = self.kwargs['symbol']
        data = requests.get(f'http://130.185.120.115:5000/api/v1/rsi_smi/db?symbol={symbol}&time_frame={time_frame}')
        crypto_data = data.json()
        crypto_name = crypto_data[list(crypto_data.keys())[1]]
        crypto_time_frame = crypto_data[list(crypto_data.keys())[2]]
        crypto_data = crypto_data[list(crypto_data.keys())[3]]
        last_action = crypto_data[list(crypto_data.keys())[0]][-1]
        back_test = crypto_data[list(crypto_data.keys())[1]]
        action_count = len(crypto_data[list(crypto_data.keys())[0]])

        response = {
            'crypto_name': crypto_name,
            'crypto_time_frame': crypto_time_frame,
            'last_action': last_action,
            'back_test': back_test,
            'action_count': action_count,

        }
        return JsonResponse(response)


'''
RSI_SMI Algorithm for each crypto,getting data from core 
show all action of 1day and 4hour time frame of the crypto
'''


class RsiMsiAlgorithmAllActions(generics.ListAPIView):
    def get(self, request, **kwargs):
        time_frame = self.kwargs['time_frame']
        symbol = self.kwargs['symbol']
        data = requests.get(f'http://130.185.120.115:5000/api/v1/rsi_smi/db?symbol={symbol}&time_frame={time_frame}')
        crypto_data = data.json()
        crypto_name = crypto_data[list(crypto_data.keys())[1]]
        crypto_time_frame = crypto_data[list(crypto_data.keys())[2]]
        crypto_data = crypto_data[list(crypto_data.keys())[3]]
        actions = crypto_data[list(crypto_data.keys())[0]]
        back_test = crypto_data[list(crypto_data.keys())[1]]
        action_count = len(crypto_data[list(crypto_data.keys())[0]])

        response = {
            'crypto_name': crypto_name,
            'crypto_time_frame': crypto_time_frame,
            'actions': actions,
            'back_test': back_test,
            'action_count': action_count,

        }
        return JsonResponse(response)


'''
MACD Algorithm for each crypto,getting data from core 
show last action of 1day and 4hour time frame of the crypto
'''


class MACDAlgorithm(generics.ListAPIView):
    def get(self, request, **kwargs):
        time_frame = self.kwargs['time_frame']
        symbol = self.kwargs['symbol']
        data = requests.get(f'http://130.185.120.115:5000/api/v1/macd/db?symbol={symbol}&time_frame={time_frame}')
        crypto_data = data.json()
        crypto_name = crypto_data[list(crypto_data.keys())[1]]
        crypto_time_frame = crypto_data[list(crypto_data.keys())[2]]
        result_MACD = crypto_data[list(crypto_data.keys())[3]]
        back_test_macd = result_MACD[list(result_MACD.keys())[1]]
        last_action_macd = result_MACD[list(result_MACD.keys())[0]][-1]
        action_count_macd = len(result_MACD[list(result_MACD.keys())[0]])
        response = {
            'crypto_name': crypto_name,
            'crypto_time_frame': crypto_time_frame,
            'back_test_macd': back_test_macd,
            'last_action_macd': last_action_macd,
            'action_count_macd': action_count_macd,

        }
        return JsonResponse(response)


'''
MACD Algorithm for each crypto,getting data from core 
show all action of 1day and 4hour time frame of the crypto
'''


class MACDAlgorithmAllActions(generics.ListAPIView):
    def get(self, request, **kwargs):
        time_frame = self.kwargs['time_frame']
        symbol = self.kwargs['symbol']
        data = requests.get(f'http://130.185.120.115:5000/api/v1/macd/db?symbol={symbol}&time_frame={time_frame}')
        crypto_data = data.json()
        crypto_name = crypto_data[list(crypto_data.keys())[1]]
        crypto_time_frame = crypto_data[list(crypto_data.keys())[2]]
        result_MACD = crypto_data[list(crypto_data.keys())[3]]
        back_test_macd = result_MACD[list(result_MACD.keys())[1]]
        actions = result_MACD[list(result_MACD.keys())[0]]
        action_count_macd = len(result_MACD[list(result_MACD.keys())[0]])
        response = {
            'crypto_name': crypto_name,
            'crypto_time_frame': crypto_time_frame,
            'back_test_macd': back_test_macd,
            'actions': actions,
            'action_count_macd': action_count_macd,

        }
        return JsonResponse(response)


'''
RSI Algorithm for each crypto,getting data from core 
show last action of 1day and 4hour time frame of the crypto
'''


class RSIAlgorithm(generics.ListAPIView):
    def get(self, request, **kwargs):
        time_frame = self.kwargs['time_frame']
        symbol = self.kwargs['symbol']
        data = requests.get(f'http://130.185.120.115:5000/api/v1/rsi/db?symbol={symbol}&time_frame={time_frame}')
        crypto_data = data.json()
        result_RSI = crypto_data[list(crypto_data.keys())[3]]
        crypto_name = crypto_data[list(crypto_data.keys())[1]]
        crypto_time_frame = crypto_data[list(crypto_data.keys())[2]]
        back_test_rsi = result_RSI[list(result_RSI.keys())[1]]
        last_action_rsi = result_RSI[list(result_RSI.keys())[0]][-1]
        action_count_rsi = len(result_RSI[list(result_RSI.keys())[0]])
        response = {
            'crypto_name': crypto_name,
            'crypto_time_frame': crypto_time_frame,
            'back_test_rsi': back_test_rsi,
            'last_action_rsi': last_action_rsi,
            'action_count_rsi': action_count_rsi,

        }
        return JsonResponse(response)


'''
RSI Algorithm for each crypto,getting data from core 
show all action of 1day and 4hour time frame of the crypto
'''


class RSIAlgorithmAllActions(generics.ListAPIView):
    def get(self, request, **kwargs):
        time_frame = self.kwargs['time_frame']
        symbol = self.kwargs['symbol']
        data = requests.get(f'http://130.185.120.115:5000/api/v1/rsi/db?symbol={symbol}&time_frame={time_frame}')
        crypto_data = data.json()
        result_RSI = crypto_data[list(crypto_data.keys())[3]]
        crypto_name = crypto_data[list(crypto_data.keys())[1]]
        crypto_time_frame = crypto_data[list(crypto_data.keys())[2]]
        back_test_rsi = result_RSI[list(result_RSI.keys())[1]]
        actions = result_RSI[list(result_RSI.keys())[0]]
        action_count_rsi = len(result_RSI[list(result_RSI.keys())[0]])
        response = {
            'crypto_name': crypto_name,
            'crypto_time_frame': crypto_time_frame,
            'back_test_rsi': back_test_rsi,
            'actions': actions,
            'action_count_rsi': action_count_rsi,

        }
        return JsonResponse(response)


'''
STOCH_RSI Algorithm for each crypto,getting data from core 
show last action of 1day and 4hour time frame of the crypto
'''


class STOCHRSIAlgorithm(generics.ListAPIView):
    def get(self, request, **kwargs):
        time_frame = self.kwargs['time_frame']
        symbol = self.kwargs['symbol']
        data = requests.get(f'http://130.185.120.115:5000/api/v1/stoch_rsi/db?symbol={symbol}&time_frame={time_frame}')
        crypto_data = data.json()
        result_STOCH_RSI = crypto_data[list(crypto_data.keys())[3]]
        crypto_name = crypto_data[list(crypto_data.keys())[1]]
        crypto_time_frame = crypto_data[list(crypto_data.keys())[2]]
        back_test_stoch_rsi = result_STOCH_RSI[list(result_STOCH_RSI.keys())[1]]
        actions = result_STOCH_RSI[list(result_STOCH_RSI.keys())[0]][-1]
        action_count_stoch_rsi = len(result_STOCH_RSI[list(result_STOCH_RSI.keys())[0]])
        response = {
            'crypto_name': crypto_name,
            'crypto_time_frame': crypto_time_frame,
            'back_test_stoch_rsi': back_test_stoch_rsi,
            'actions': actions,
            'action_count_stoch_rsi': action_count_stoch_rsi,

        }
        return JsonResponse(response)


'''
STOCH_RSI Algorithm for each crypto,getting data from core 
show all action of 1day and 4hour time frame of the crypto
'''


class STOCHRSIAlgorithmAllActions(generics.ListAPIView):
    def get(self, request, **kwargs):
        time_frame = self.kwargs['time_frame']
        symbol = self.kwargs['symbol']
        data = requests.get(f'http://130.185.120.115:5000/api/v1/stoch_rsi/db?symbol={symbol}&time_frame={time_frame}')
        crypto_data = data.json()
        result_STOCH_RSI = crypto_data[list(crypto_data.keys())[3]]
        crypto_name = crypto_data[list(crypto_data.keys())[1]]
        crypto_time_frame = crypto_data[list(crypto_data.keys())[2]]
        back_test_stoch_rsi = result_STOCH_RSI[list(result_STOCH_RSI.keys())[1]]
        last_action_stoch_rsi = result_STOCH_RSI[list(result_STOCH_RSI.keys())[0]]
        action_count_stoch_rsi = len(result_STOCH_RSI[list(result_STOCH_RSI.keys())[0]])
        response = {
            'crypto_name': crypto_name,
            'crypto_time_frame': crypto_time_frame,
            'back_test_stoch_rsi': back_test_stoch_rsi,
            'last_action_stoch_rsi': last_action_stoch_rsi,
            'action_count_stoch_rsi': action_count_stoch_rsi,

        }
        return JsonResponse(response)


'''
Show all algorithm of each crypto in 1day and 4hours time frame
'''


class AllAlgorithmSymbol(generics.ListAPIView):
    def get(self, request, **kwargs):
        time_frame = self.kwargs['time_frame']
        symbol = self.kwargs['symbol']
        data = requests.get(
            f'http://130.185.120.115:5000/api/v1/all_algorithms/db?symbol={symbol}&time_frame={time_frame}')
        crypto_data = data.json()
        crypto_name = crypto_data[list(crypto_data.keys())[0]]
        crypto_time_frame = crypto_data[list(crypto_data.keys())[1]]
        '''
        Return MACD strategy
        '''
        result_MACD = crypto_data[list(crypto_data.keys())[2]]
        message_macd = result_MACD[list(result_MACD.keys())[0]]
        back_test_macd = result_MACD[list(result_MACD.keys())[2]]
        last_action_macd = result_MACD[list(result_MACD.keys())[1]][-1]
        action_count_macd = len(result_MACD[list(result_MACD.keys())[1]])

        '''
        Return RSI strategy
        '''
        result_RSI = crypto_data[list(crypto_data.keys())[3]]
        message_rsi = result_RSI[list(result_RSI.keys())[0]]
        back_test_rsi = result_RSI[list(result_RSI.keys())[2]]
        last_action_rsi = result_RSI[list(result_RSI.keys())[1]][-1]
        action_count_rsi = len(result_RSI[list(result_RSI.keys())[1]])

        '''
        Return RSI_SMI strategy
        '''
        result_RSI_SMI = crypto_data[list(crypto_data.keys())[4]]
        message_rsi_smi = result_RSI_SMI[list(result_RSI_SMI.keys())[0]]
        back_test_rsi_smi = result_RSI_SMI[list(result_RSI_SMI.keys())[2]]
        last_action_rsi_smi = result_RSI_SMI[list(result_RSI_SMI.keys())[1]][-1]
        action_count_rsi_smi = len(result_RSI_SMI[list(result_RSI_SMI.keys())[1]])
        '''
        Return STOCH_RSI strategy
        '''
        result_STOCH_RSI = crypto_data[list(crypto_data.keys())[5]]
        message_stoch_rsi = result_STOCH_RSI[list(result_STOCH_RSI.keys())[0]]
        back_test_stoch_rsi = result_STOCH_RSI[list(result_STOCH_RSI.keys())[2]]
        last_action_stoch_rsi = result_STOCH_RSI[list(result_STOCH_RSI.keys())[1]][-1]
        action_count_stoch_rsi = len(result_STOCH_RSI[list(result_STOCH_RSI.keys())[1]])

        response = {
            'crypto_name': crypto_name,
            'crypto_time_frame': crypto_time_frame,
            'message_macd': message_macd,
            'back_test_macd': back_test_macd,
            'last_action_macd': last_action_macd,
            'action_count_macd': action_count_macd,
            'message_rsi': message_rsi,
            'back_test_rsi': back_test_rsi,
            'last_action_rsi': last_action_rsi,
            'action_count_rsi': action_count_rsi,
            'message_rsi_smi': message_rsi_smi,
            'back_test_rsi_smi': back_test_rsi_smi,
            'last_action_rsi_smi': last_action_rsi_smi,
            'action_count_rsi_smi': action_count_rsi_smi,
            'message_stoch_rsi': message_stoch_rsi,
            'back_test_stoch_rsi': back_test_stoch_rsi,
            'last_action_stoch_rsi': last_action_stoch_rsi,
            'action_count_stoch_rsi': action_count_stoch_rsi,

        }
        return JsonResponse(response)


class AllAlgorithEachSymbol(generics.ListAPIView):
    def get(self, request, **kwargs):
        time_frame = self.kwargs['time_frame']
        symbol = self.kwargs['symbol']
        data = requests.get(
            f'http://130.185.120.115:5000/api/v1/all_algorithms/db?symbol={symbol}&time_frame={time_frame}')
        crypto_data = data.json()
        crypto_name = crypto_data[list(crypto_data.keys())[0]]
        '''
        Return MACD strategy
        '''
        result_MACD = crypto_data[list(crypto_data.keys())[2]]
        last_action = result_MACD[list(result_MACD.keys())[1]][-1]
        price_macd = last_action[list(last_action.keys())[0]]
        action_macd = last_action[list(last_action.keys())[1]]
        date_macd = last_action[list(last_action.keys())[2]]
        back_test_macd = result_MACD[list(result_MACD.keys())[2]]

        '''
        Return RSI strategy
        '''

        result_RSI = crypto_data[list(crypto_data.keys())[3]]
        last_action = result_RSI[list(result_RSI.keys())[1]][-1]
        price_rsi = last_action[list(last_action.keys())[0]]
        action_rsi = last_action[list(last_action.keys())[1]]
        date_rsi = last_action[list(last_action.keys())[2]]
        back_test_rsi = result_RSI[list(result_RSI.keys())[2]]

        '''
        Return RSI_SMI strategy
        '''
        result_RSI_SMI = crypto_data[list(crypto_data.keys())[4]]
        last_action = result_RSI_SMI[list(result_RSI_SMI.keys())[1]][-1]
        price_rsi_smi = last_action[list(last_action.keys())[0]]
        action_rsi_smi = last_action[list(last_action.keys())[1]]
        date_rsi_smi = last_action[list(last_action.keys())[2]]
        back_test_rsi_smi = result_RSI_SMI[list(result_RSI_SMI.keys())[2]]

        '''
        Return STOCH_RSI strategy
        '''
        STOCH_RSI = crypto_data[list(crypto_data.keys())[5]]
        last_action = STOCH_RSI[list(STOCH_RSI.keys())[1]][-1]
        price_stoch_rsi = last_action[list(last_action.keys())[0]]
        action_stoch_rsi = last_action[list(last_action.keys())[1]]
        date_stoch_rsi = last_action[list(last_action.keys())[2]]
        back_test_stoch_rsi = STOCH_RSI[list(STOCH_RSI.keys())[2]]

        response = {
            'crypto_name': crypto_name,
            'price_macd': price_macd,
            'action_macd': action_macd,
            'date_macd': date_macd,
            'back_test_macd': back_test_macd,
            'price_rsi': price_rsi,
            'action_rsi': action_rsi,
            'date_rsi': date_rsi,
            'back_test_rsi': back_test_rsi,
            'price_rsi_smi': price_rsi_smi,
            'action_rsi_smi': action_rsi_smi,
            'date_rsi_smi': date_rsi_smi,
            'back_test_rsi_smi': back_test_rsi_smi,
            'price_stoch_rsi': price_stoch_rsi,
            'action_stoch_rsi': action_stoch_rsi,
            'date_stoch_rsi': date_stoch_rsi,
            'back_test_stoch_rsi': back_test_stoch_rsi,

        }
        return JsonResponse(response)


class PriceHistory(generics.ListAPIView):
    def get(self, request, **kwargs):
        time_frame = self.kwargs['time_frame']
        symbol = self.kwargs['symbol']
        data = requests.get(
            f'http://130.185.120.115:5000/api/v1/price_history/price_history?symbol={symbol}&time_frame={time_frame}'
            f'&limit=100')
        crypto_data = data.json()
        return JsonResponse(crypto_data)


class ImageView(generics.RetrieveAPIView):

    def get(self, request, **kwargs):
        symbol = self.kwargs['symbol']
        print(symbol)
        assets = Assets.objects.get(name=symbol)
        image = assets.image
        return HttpResponse(image)


class AllDataView(generics.ListAPIView):

    def get(self, request, **kwargs):
        symbol = self.kwargs['symbol']
        time_frame = self.kwargs['time_frame']
        data = requests.get(
            f'http://130.185.120.115:5000/api/v1/all_data/all_data?symbol={symbol}&time_frame={time_frame}'
            f'&limit=100')
        crypto_data = data.json()
        crypto_name = crypto_data[list(crypto_data.keys())[0]]
        time_frame = crypto_data[list(crypto_data.keys())[1]]
        latest_price = crypto_data[list(crypto_data.keys())[2]]
        current_price = latest_price[list(latest_price.keys())[0]]
        volume_24 = latest_price[list(latest_price.keys())[1]]
        amount = latest_price[list(latest_price.keys())[2]]
        market_cap = latest_price[list(latest_price.keys())[3]]
        price_history = crypto_data[list(crypto_data.keys())[3]]
        response = {
            'crypto_name': crypto_name,
            'time_frame': time_frame,
            'current_price': current_price,
            'volume_24': volume_24,
            'amount': amount,
            'market_cap': market_cap,
            'price_history': price_history,

        }
        return JsonResponse(response)


class MarketList(generics.ListAPIView):
    def get(self, request, **kwargs):
        data = requests.get('http://130.185.120.115:5000/api/v1/market_list/market_list')

        crypto_data = data.json()
        return JsonResponse(crypto_data)
