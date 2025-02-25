from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.views import PasswordResetConfirmView
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    # For email confirmation - you might want to customize this template
    path('email-confirmation-success/', TemplateView.as_view(template_name="account/email_confirmation_success.html"), 
         name='account_email_confirmation_success'),
    # Ensure we have a route for password reset confirm
    path('api/auth/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]


