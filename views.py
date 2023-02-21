from django.shortcuts import render
from django.http import HttpResponse
from .models import UserProfile
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import UserProfileSerializer


# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

def Cunnect_header(request):
    return HttpResponse('<b style="color:orange">Cunnect <b> <b style="color:blue">App </b>')
    