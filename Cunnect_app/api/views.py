
from .models import UserProfile, User
from django.contrib.auth import login

from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from .serializer import UserSerializer, UserProfileSerializer, RegisterSerializer, LoginSerializer
import re


# Create your views here.


#UserProfile view set defines the view behavior 
class UserProfileViewSet(viewsets.ModelViewSet): #This line of code defines a class called UserProfileViewSet, which is used to handle requests related to user profiles.
    queryset = UserProfile.objects.all() #This line of code sets the initial queryset for the UserProfileViewSet to include all user profiles in the database.
    serializer_class = UserProfileSerializer #This line of code sets the serializer class that should be used to convert UserProfile objects to JSON format.
    permission_classes = [permissions.AllowAny]

#CUNY student register viewset
class RegisterViewset(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer 
    queryset = User.objects.all() #This line of code sets the initial queryset for the RegisterViewset to include all user accounts in the database.
    permission_classes = [permissions.AllowAny] # sets the permissions for who can access the RegisterViewset to be "allow any", which means that anyone can register as a new user.
    def create(self, request): #function handles the creation of new user accts
        serializer = RegisterSerializer(data = request.data) # creates a new instance of the RegisterSerializer class using the request data that was submitted when the user registered.

        if serializer.is_valid():
            user = serializer.save() #saves the new user account to the database.

            #return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data, #
            "token": AuthToken.objects.create(user)[1]
        })
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#login viewset

class LoginAPI(viewsets.ModelViewSet):
    serializer_class = LoginSerializer # Use our custom LoginSerializer for serialization 
    queryset = User.objects.all() 
    permission_classes = [permissions.AllowAny] # Allow any user to access this view  
    def create(self, request):
        serializer = LoginSerializer(data = request.data) # Instantiate our LoginSerializer with the request data
        serializer.is_valid(raise_exception= True) # Validate the serializer data, raising an exception if it fails
        user = serializer.validated_data['user'] # Get the user object from the serializer's validated data
        login(request, user)  # Log the user in using Django's built-in login function
        return Response({'token': AuthToken.objects.create(user)[1],  # Generate an authentication token for the user using Knox's AuthToken, and add it to the response data
            'user_id': user.pk, # Add the user's ID to the response data
            'user_first_name': user.first_name, # Add the user's first & last name to the response data
            'user_last_name' : user.last_name
            })

