from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from dj_rest_auth.views import UserDetailsView
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.models import SocialAccount
from .serializers import CustomUserDetailsSerializer, SocialAccountSerializer

class CustomUserDetailsView(UserDetailsView):
    """
    Extended user details view with custom serializer
    """
    serializer_class = CustomUserDetailsSerializer

class GoogleLogin(SocialLoginView):
    """
    Google OAuth2 login endpoint configuration
    """
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = "http://localhost:8000/api/auth/google/callback/"

class FacebookLogin(SocialLoginView):
    """
    Facebook OAuth2 login endpoint configuration
    """
    adapter_class = FacebookOAuth2Adapter
    client_class = OAuth2Client
    callback_url = "http://localhost:8000/api/auth/facebook/callback/"

class GitHubLogin(SocialLoginView):
    """
    GitHub OAuth2 login endpoint configuration 
    """
    adapter_class = GitHubOAuth2Adapter
    client_class = OAuth2Client
    callback_url = "http://localhost:8000/api/auth/github/callback/"

class SocialAccountList(generics.ListAPIView):
    """List view for user's social accounts"""
    serializer_class = SocialAccountSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Filter social accounts by current user"""
        return SocialAccount.objects.filter(user=self.request.user)