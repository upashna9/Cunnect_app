from django.urls import path, include
from . import views
from rest_framework import routers
#this is our push
router = routers.DefaultRouter()
router.register(r'UserProfile', views.UserProfileViewSet)
#python list of paths we can access
urlpatterns = [
    #path('', include(router.urls)), 
    #path('api-auth/', include('rest_framework.urls')),
    path('', views.Cunnect_header, name = 'tasks')
]
