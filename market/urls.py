from market.views import CreatePortfolioApiView, ActiveComment, LikeViewSet, DisLikeViewSet, \
    PortfolioList, CommentViewSet, MarketDetail, MarketList, PortfolioDetailDestroy, PortfolioNameUpdate, \
    PortfolioAssetsUpdate, AssetsDetail, LatestPriceViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include, path

router = DefaultRouter()
router.register("market_list", MarketList, basename="market_list")
router.register("market_detail", MarketDetail, basename="market_detail")
router.register("create_portfolio", CreatePortfolioApiView, basename="create_portfolio")
router.register("Portfolio_list", PortfolioList, basename="Portfolio_list")
router.register("Portfolio_Detail", PortfolioDetailDestroy, basename="Portfolio_Detail")
router.register("active_comments", ActiveComment, basename="active_comments")
router.register("comments", CommentViewSet, basename="comments")
router.register("like", LikeViewSet, basename="like")
router.register("dislike", DisLikeViewSet, basename="dislike")
router.register("portfolio_name_update", PortfolioNameUpdate, basename="portfolio_name_update")
router.register("portfolio_assets_update", PortfolioAssetsUpdate, basename="portfolio_assets_update")
router.register("assets_detail", AssetsDetail, basename="assets_detail")
router.register("latest_price", LatestPriceViewSet, basename="latest_price")

urlpatterns = [
    path('', include(router.urls)),

]
