from rest_framework.routers import DefaultRouter

from paper_trading.views import *

from django.urls import path, include

router = DefaultRouter()

router.register("create_paper_trading", CreatePaperTradingApiView, basename="create_paper_trading")
router.register("paper_trading_list", PaperTradingListApiView, basename="paper_trading_list")
router.register("paper_trading_detail", PaperTradingDetailApiView, basename="paper_trading_detail")
router.register("paper_trading_delete", PaperTradingDestroyApiView, basename="paper_trading_delete")
router.register("paper_update_detail", PaperPartialUpdateApiView, basename="paper_update_detail")
# router.register("change_status", ChangStatusApiView, basename="change_status")
router.register("paper_difference", PaperTradingApiView, basename="paper_difference")
router.register("history_paper_trading", HistoryAllPaperTradingApiView, basename="history_paper_trading")
router.register("history_specified_paper_trading", HistorySpecifiedPaperTradingApiView,
                basename="history_specified_paper_trading")
router.register("submit_paper", SubmitPaperTradingApiView, basename="submit_paper")

urlpatterns = [
    path('', include(router.urls)),
]
