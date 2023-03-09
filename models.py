from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from django.utils import timezone
from Cunnect_app.models import CustomUser
from django.contrib.auth import get_user_model
#defining a custom manager for the User model
class CustomUserManager(BaseUserManager):
    #function for creating a user
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The email must be set')
        if not username:
            raise ValueError('The username must be set')
        
        #lowercase domain of email
        email = self.normalize_email(email) 
        user = self.model(email = email, username = username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
        
#defining user model

class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(blank=True, upload_to='profile_pictures')
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.username

#defining post model for posts on a users personal profile
class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    media = models.FileField(upload_to= 'post_media/', null= True, blank = True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.author}: {self.content}"

#defining a message model for messaging system between user and their friends
"""This model has a foreign key to the User model, which can be accessed using get_user_model() 
to ensure compatibility with custom user models. The related_name parameter on the foreign 
key fields allows you to access the messages sent and received by a user by calling 
user.sent_messages.all() or user.received_messages.all()."""
class Message(models.Model):
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.content}"