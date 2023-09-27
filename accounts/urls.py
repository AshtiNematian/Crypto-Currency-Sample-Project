from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change_pass/<int:pk>', ChangePasswordView.as_view(),name='change_pass'),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='details'),
    path("forget_password_email", PasswordReset.as_view(), name="request-password-reset", ),
    path("forget_password/<str:encoded_pk>/<str:token>/", ResetPasswordAPI.as_view(), name="reset-password", )

]
