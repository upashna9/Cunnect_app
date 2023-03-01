from django.urls import path, include
from . import views
from rest_framework import routers
# URLs are used to map URLs to views. In Django, you can define URL patterns that
#  map specific URLs to specific views.
router = routers.DefaultRouter()
router.register(r'UserProfile', views.UserProfileViewSet)
#python list of paths we can access
urlpatterns = [
    path('', include(router.urls)), 
    path('api-auth/', include('rest_framework.urls')),
    path('api/UserCreate/', views.RegisterViewSet.as_view(), name = "UserCreate" )
    #path('register/', RegisterUserView.as_view(), name='register'),
    #path('login/', obtain_auth_token, name='login'),
    #path('logout/', LogoutView.as_view(), name='logout'),
    #path('', views.Cunnect_header, name = 'tasks')
]