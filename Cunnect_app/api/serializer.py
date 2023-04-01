from .models import User, UserProfile, Posts
from rest_framework import serializers
from django.contrib.auth import authenticate

import re

#serializers define the API representation

#User serializer 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['cuny_email', 'first_name', 'last_name','major', 'CUNY', 'graduation_year', 'birth_date']
# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style = {'input_type':'password'}, write_only = True)

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'cuny_email', 'password', 'password2', 'major', 'CUNY', 'graduation_year', 'birth_date']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            username = self.validated_data['username'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            cuny_email = self.validated_data['cuny_email'],
            major = self.validated_data['major'],
            CUNY = self.validated_data['CUNY'],
            graduation_year = self.validated_data['graduation_year'],
            birth_date = self.validated_data['birth_date']
            )
        password = self.validated_data['password']
        password2 = self.validated_data['password2'] 
        
    
        if not re.search(r'\.cuny\.edu$', self.validated_data.get('cuny_email')):
            raise serializers.ValidationError("Must use a CUNY email to register")
        

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        
        user.set_password(password)
        user.save()
        
        profile = UserProfile(
            user=user,
            #cuny_email=self.validated_data['cuny_email'],
            major=self.validated_data.get('major'),
            CUNY=self.validated_data.get('CUNY'),
            birth_date=self.validated_data.get('birth_date')
        )
        
        profile.save()
        return user
    
#login serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username = data['username'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect email or password')
    

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'CUNY','major','birth_date', 'profile_pic', 'date_user_joined']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['user', 'image', 'caption', 'date_created']