from .models import UserProfile, User
from rest_framework import viewsets
from rest_framework import generics, permissions
from rest_framework.response import Response
#from django.contrib.auth.models import User
from django.core.mail import send_mail
#from .serializer import UserSerializer
from knox.models import AuthToken
from .serializer import UserSerializer, UserProfileSerializer, RegisterSerializer


# Create your views here.
#UserCreate is the class view set when a CUNY student wants to register an account into the app
"""
class RegisterViewSet(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    def perform_create(self, serializer):
        email = serializer.validated_data.get('email')
        if email.endswith('.cuny.edu'):
            verification_code = '123456' # You can generate a random verification code here
            send_mail(
                'Email Verification Code',
                f'Your verification code is {verification_code}.',
                'from@example.com',
                [email],
                fail_silently=False,
            )
            serializer.save()
            return Response({'success': 'Verification code has been sent to your email.'})
        else:
            return Response({'error': 'Only email addresses with .cuny.edu domain are allowed.'})
"""
# Register API for CUNY student registering basically a request sent from the frontend for a
#CUNY student who wants to register. this register class will handle the request and perform this response

class RegisterViewSet(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny] #basically allow anyone to view this viewset
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

#UserProfile view set defines the view behavior 
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.BasePermission]
    
