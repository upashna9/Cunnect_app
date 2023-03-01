from .models import User, UserProfile
from rest_framework import serializers

#serializers define the API representation

#User serializer 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['cuny_email', 'username', 'major', 'CUNY', 'graduation_year', 'birth_date']
# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['cuny_email', 'username', 'major', 'CUNY', 'graduation_year', 'birth_date'] 
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['cuny_email'], validated_data['password'])
        return user
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'CUNY', 'birth_date', 'profile_pic', 'date_user_joined']