from django.db import models
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount

class UserProfile(models.Model):
    """
    Extended user profile model with additional user information
    - One-to-one relationship with Django User model
    - Stores bio, location, birth date, and profile picture
    - Provides access to linked social accounts
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    
    def __str__(self):
        """
        String representation using username
        """
        return self.user.username
    
    @property
    def social_accounts(self):
        """
        Property to access linked social accounts
        """
        return SocialAccount.objects.filter(user=self.user)
