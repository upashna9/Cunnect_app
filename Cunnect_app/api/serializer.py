from .models import User, UserProfile
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
    confirm_password = serializers.CharField(style = {'input_type':'password'}, write_only = True)

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'cuny_email', 'password', 'confirm_password', 'major', 'CUNY', 'graduation_year', 'birth_date']
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
        confirm_password = self.validated_data['confirm_password'] 
        
    
        if not re.search(r'\.cuny\.edu$', self.validated_data.get('cuny_email')):
            raise serializers.ValidationError("Must use a CUNY email to register")
        

        if password != confirm_password:
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
class LoginSerializer(serializers.Serializer): #inherits from the serializers.Serializer class.
    username = serializers.CharField() # these lines define the fields that are expected in the input data when the serializer is used, 
    password = serializers.CharField()

#This method is called when the serializer is used to validate input data, and it is responsible for performing any additional 
#validation that is needed beyond the basic field-level validation provided by the serializer
    def validate(self, data):  
        #authenticate function takes a username and password and returns a user object if the credentials are valid and the user is active
        user = authenticate(username = data['username'], password=data['password']) 
        if user and user.is_active:
            return {'user': user}
        raise serializers.ValidationError('Incorrect email or password')
"""Overall, this serializer expects input data containing a username and password field, and validates 
these fields by attempting to authenticate the user using Django's built-in authentication system. If the credentials are valid, 
the serializer returns a dictionary containing the authenticated user object, otherwise it raises a ValidationError."""   

class UserProfileSerializer(serializers.ModelSerializer):
#The Meta class specifies some metadata for the serializer, such as the model that it serializes (UserProfile) and the 
#fields that it includes in its serialized representation (specified by the fields attribute)
    class Meta: 
        model = UserProfile 
        fields = ['user', 'bio', 'CUNY','major','birth_date', 'profile_pic', 'date_user_joined']

"""So, overall, this serializer will be used to serialize instances of the UserProfile model, and the serialized representation will 
include the user, bio, CUNY, major, birth_date, profile_pic, and date_user_joined fields of the model."""