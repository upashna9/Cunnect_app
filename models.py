from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User
# Create your models here.
"""This class will help django work with our custom user model"""

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    CUNY = models.CharField(max_length=30, blank=False)
    birth_date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    date_user_joined = models.DateTimeField(auto_now_add= True)

    def __str__(self): #self represents the userprofile model
        return self.user.username

#create a model class for a Post on a social media ios app using django where the post displays the post's image, post's caption and post's likes.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_pics', blank=True)
    caption = models.TextField(max_length=500, blank=True)
    likes = models.IntegerField(default=0)
#class UserManager(models.Model):
    #use_in_migrations = True
    #"""This function will create a new user profile object"""
    #def create_user(self, name, cuny_email, password):
        #if not cuny_email:
           # raise ValueError('Must have a valid CUNY student email')

      #  if not name:
         #   raise ValueError('Must have a name as a CUNY student')
       # if not password:
          #  raise ValueError('Must have a password')
        
       # cuny_email = self.normalize_email(cuny_email)
        #name = name.strip()
       # user = self.model(name = name, cuny_email = cuny_email)
       # user.set_password(password)
       # user.save(using = self._db)

#class User(AbstractBaseUser):
   # name = models.charfield(length = 255)
