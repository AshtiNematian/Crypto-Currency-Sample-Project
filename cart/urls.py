from django.urls import include, path
from rest_framework import routers
from cart import views

router = routers.DefaultRouter()
router.register('coupon', views.CouponViewSet, basename="coupon")
router.register('user_cart', views.CartViewSet, basename="user_cart")
urlpatterns = [
    path('', include(router.urls)),
]
