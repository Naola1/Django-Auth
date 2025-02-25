from django.db import models
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
    @property
    def social_accounts(self):
        return SocialAccount.objects.filter(user=self.user)