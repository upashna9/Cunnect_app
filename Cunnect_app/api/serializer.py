from .models import User, UserProfile, Posts, Comment, Likes
from rest_framework import serializers
from django.contrib.auth import authenticate

import re

#serializers define the API representation
#User serializer 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = User
        fields = ['cuny_email', 'first_name', 'last_name', 'major', 'CUNY', 'graduation_year', 'birth_date']
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

class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    num_likes = serializers.SerializerMethodField()
    users_who_liked = serializers.SerializerMethodField()
    class Meta:
        model = Posts
        fields = ['user', 'image', 'caption', 'date_created', 'num_likes', 'comments', 'users_who_liked']
    #self represents the specific instance of the postserializer class thats being used to serialize a post object
    #obj represents the specific instance of the post model that is being serialized
    #the function num_likes returns the number of likes of a specific post instance by calling the num_likes function in the post model
    def get_num_likes(self, obj):
        return obj.num_likes()
    
    #self represents the specific instance of the post serializer class
    #obj represents the specific instance of the post model that is being serialized
    #the function get_users_who_liked returns a list of the users first_name and last_name who liked the post
    def get_users_who_liked(self, obj):
        return [User.first_name for User in obj.users_who_liked()]
    
    #self represents the specific instance of the post serializer class
    #obj represents the specific instance of the post model that is being serialized
    #the function defines the_comments variable by calling the comments function that returns all the comments of the specific post model
    #we return the serialized data of the list of comments by calling the Commentserializer on the list of comments and returning them
    def get_comments(self, obj):
        the_comments = obj.comments()
        return CommentSerializer(the_comments, many = True).data

"""So, overall, this serializer will be used to serialize instances of the UserProfile model, and the serialized representation will 
include the user, bio, CUNY, major, birth_date, profile_pic, and date_user_joined fields of the model."""

"""The class CommentSerializer(serializers.ModelSerializer): line creates a new serializer called CommentSerializer that inherits from 
serializers.ModelSerializer. The next four lines define the fields that should be included in the serialized representation of a Comment
 object. In this case, were including the id, user, post, and content fields."""
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'user', 'text', 'created_at']

"""This block of code defines the serializer for the Like model. The class LikeSerializer(serializers.ModelSerializer): line creates a new 
serializer called LikeSerializer that inherits from serializers.ModelSerializer. The next three lines define the fields that should be included in 
the serialized representation of a Like object. In this case, were including the id, user, and post fields."""
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ['post', 'user']