from django.urls import path, include
from rest_framework.routers import DefaultRouter

from membership.views import MemberShipViewList, MemberShipDetail, MembershipView, CreateUserMembershipApiView

router = DefaultRouter()
router.register("membership_list", MemberShipViewList, basename="membership_list")
router.register("membership_detail", MemberShipDetail, basename="membership_detail")
router.register("user_membership", MembershipView, basename="user_membership")
router.register("create_membership", CreateUserMembershipApiView, basename="create_membership")


urlpatterns = [
    path('', include(router.urls)),

]

