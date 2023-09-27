from django.urls import path
from feature.views import AllAlgorithmSymbol, AllAlgorithEachSymbol, RsiMsiAlgorithm, MACDAlgorithm, RSIAlgorithm, \
    STOCHRSIAlgorithm, PriceHistory, RsiMsiAlgorithmAllActions, MACDAlgorithmAllActions, RSIAlgorithmAllActions, \
    STOCHRSIAlgorithmAllActions, AllDataView, ImageView, MarketList

urlpatterns = [
    path('rsi_smi_algorithm/<symbol>/<time_frame>', RsiMsiAlgorithm.as_view(), name='rsi_smi_algorithm'),
    path('rsi_smi_all_actions/<symbol>/<time_frame>', RsiMsiAlgorithmAllActions.as_view(), name='rsi_smi_all_actions'),
    path('macd_algorithms/<symbol>/<time_frame>', MACDAlgorithm.as_view(), name='macd_algorithms'),
    path('macd_all_actions/<symbol>/<time_frame>', MACDAlgorithmAllActions.as_view(), name='macd_algorithm'),
    path('rsi_algorithms/<symbol>/<time_frame>', RSIAlgorithm.as_view(), name='rsi_algorithms'),
    path('rsi_all_actions/<symbol>/<time_frame>', RSIAlgorithmAllActions.as_view(), name='rsi_all_actions'),
    path('stoch_rsi_algorithms/<symbol>/<time_frame>', STOCHRSIAlgorithm.as_view(), name='stoch_rsi_algorithms'),
    path('stoch_rsi_all_actions/<symbol>/<time_frame>', STOCHRSIAlgorithmAllActions.as_view(),
         name='stoch_rsi_all_actions'),
    path('all_algorithms/<symbol>/<time_frame>', AllAlgorithmSymbol.as_view(), name='all_algorithms_of_symbol'),
    path('price_history/<symbol>/<time_frame>', PriceHistory.as_view(), name='price_history'),
    path('image/<symbol>/', ImageView.as_view(), name='image'),
    path('all_data/<symbol>/<time_frame>', AllDataView.as_view(), name='all_data'),
    path('market_list/', MarketList.as_view(), name='market_list'),
    path('all_algorithms/each/<symbol>/<time_frame>', AllAlgorithEachSymbol.as_view(),
         name='all_algorithms_each_symbol'),

]
