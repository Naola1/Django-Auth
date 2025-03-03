from django.urls import path, include
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import CustomUserDetailsView, GoogleLogin, FacebookLogin, SocialAccountList

urlpatterns = [
    # Authentication endpoints
    path('login/', LoginView.as_view(), name='rest_login'),
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('user/', CustomUserDetailsView.as_view(), name='rest_user_details'),
    
    # Password management
    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
    path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    
    # JWT management
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # Registration flow
    path('registration/', RegisterView.as_view(), name='rest_register'),
    path('registration/verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    path('registration/verify-email/<key>/', ConfirmEmailView.as_view(), name='account_confirm_email'),
    
    # Social authentication
    path('google/', GoogleLogin.as_view(), name='google_login'),
    path('facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('social-accounts/', SocialAccountList.as_view(), name='social_account_list'),
    
    # Allauth URLs
    path('', include('allauth.urls'))
]