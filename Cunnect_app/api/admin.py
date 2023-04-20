from django.contrib import admin
from .models import UserProfile, User, Posts, Likes, Comment
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(User)
admin.site.register(Likes)
admin.site.register(Comment)
admin.site.register(Posts)
