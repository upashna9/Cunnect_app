from .models import User, UserProfile
from rest_framework import serializers

#serializers define the API representation

#User serializer 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['cuny_email', 'first_name', 'last_name','major', 'CUNY', 'graduation_year', 'birth_date']
# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        password = serializers.CharField(write_only=True)
        confirm_password = serializers.CharField(write_only=True)
        fields = ['cuny_email', 'first_name', 'last_name', 'password', 'major', 'CUNY', 'graduation_year', 'birth_date'] 
        #extra_kwargs = {'password': {'write_only': True}, 'confirm_password': {'write_only': True}}

    def create(self, validated_data):
    
        user = User.objects.create_user(
        validated_data['cuny_email'],
        password=validated_data['password'],
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name'],
        major=validated_data['major'],
        CUNY=validated_data['CUNY'],
        graduation_year=validated_data['graduation_year'],
        birth_date=validated_data['birth_date'])
        return user
        
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'CUNY', 'birth_date', 'profile_pic', 'date_user_joined']