from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User(User):
    cuny_email = models.EmailField(unique = True)
    major = models.CharField(max_length=100, blank=True)
    CUNY = models.CharField(max_length=30, blank=False)
    graduation_year = models.IntegerField(blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    date_user_joined = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return self.username
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    CUNY = models.CharField(max_length=30, blank=False)
    birth_date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    date_user_joined = models.DateTimeField(auto_now_add= True)

    def __str__(self): #self represents the userprofile model
        return self.user.username
