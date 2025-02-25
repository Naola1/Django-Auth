from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile
from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.socialaccount.models import SocialAccount

class SocialAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialAccount
        fields = ('provider', 'uid', 'last_login', 'date_joined')

class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('bio', 'location', 'birth_date', 'profile_picture')

class CustomUserDetailsSerializer(UserDetailsSerializer):
    profile = UserProfileSerializer(source="profile", required=False)
    social_accounts = SocialAccountSerializer(source="profile.social_accounts", many=True, read_only=True)
    
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('profile', 'social_accounts')
    
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        instance = super().update(instance, validated_data)
        
        profile, created = UserProfile.objects.get_or_create(user=instance)
        
        if profile_data:
            if 'bio' in profile_data:
                profile.bio = profile_data.get('bio')
            if 'location' in profile_data:
                profile.location = profile_data.get('location')
            if 'birth_date' in profile_data:
                profile.birth_date = profile_data.get('birth_date')
            if 'profile_picture' in profile_data:
                profile.profile_picture = profile_data.get('profile_picture')
            profile.save()
        
        return instance