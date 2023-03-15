
from .models import UserProfile, User
from django.contrib.auth import login

from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from .serializer import UserSerializer, UserProfileSerializer, RegisterSerializer, LoginSerializer
import re


# Create your views here.


#UserProfile view set defines the view behavior 
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]

#CUNY student register viewset
class RegisterViewset(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    def create(self, request):
        serializer = RegisterSerializer(data = request.data)

        if serializer.is_valid():
            user = serializer.save()

            #return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#login viewset

class LoginAPI(viewsets.ModelViewSet):
    serializer_class = LoginSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    def create(self, request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception= True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
        """
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception= True)
        user = serializer.validated_data
        return Response({"user": UserSerializer(user).data,
                          "userprofile": UserProfileSerializer(UserProfile.objects.get(user = user)).data,
                        })
        """
