from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from dj_rest_auth.views import UserDetailsView
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.models import SocialAccount
from .serializers import CustomUserDetailsSerializer, SocialAccountSerializer

class CustomUserDetailsView(UserDetailsView):
    serializer_class = CustomUserDetailsSerializer

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = "http://localhost:8000/api/auth/google/callback/"  # Change this in production

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    client_class = OAuth2Client
    callback_url = "http://localhost:8000/api/auth/facebook/callback/"  # Change this in production

class SocialAccountList(generics.ListAPIView):
    serializer_class = SocialAccountSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return SocialAccount.objects.filter(user=self.request.user)
