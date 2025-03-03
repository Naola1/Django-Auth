from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.views import PasswordResetConfirmView
from django.views.generic import TemplateView

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Authentication API endpoints
    path('api/auth/', include('authentication.urls')),

    # Allauth URLs
    path('accounts/', include('allauth.urls')),

    # Email confirmation success page
    path('email-confirmation-success/', TemplateView.as_view(
        template_name="account/email_confirmation_success.html"
    ), name='account_email_confirmation_success'),

    # Password reset confirmation
    path('api/auth/password/reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]