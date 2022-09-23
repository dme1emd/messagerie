from dataclasses import field
from rest_framework import serializers
from discussion.models import *
from profiles.models import *
from message.models import *
class ProfileSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Profile
        fields =  ['id' , 'email' , 'username' , 'password' , 'profile_pic']

class MessageSerializer(serializers.ModelSerializer):
    sender = ProfileSerializer()
    class Meta : 
        model = Message
        fields = '__all__'
class DiscussionSerializer(serializers.ModelSerializer):
    profile_one = ProfileSerializer()
    profile_two = ProfileSerializer()
    messages = MessageSerializer(many=True)
    class Meta : 
        model = Discussion
        fields = '__all__'