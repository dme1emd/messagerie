import dis
import sre_compile
from django.shortcuts import render
from rest_framework import response , decorators , generics
from discussion.models import *
from profiles.models import *
from message.models import *
from django.db.models import Q
from .serializers import *
# Create your views here.
@decorators.api_view(['GET'])
def recent_discussions(request) : 
    discussions = Discussion.objects.filter(Q(profile_one=request.user) | Q(profile_two = request.user))
    discussions = DiscussionSerializer(discussions , many = True).data
    return response.Response(discussions , status=200)
class CreateProfileApiView(generics.CreateAPIView) :
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    def perform_create(self, serializer):
        dict = serializer.context.get('request').data
        pic = dict.get('profile_pic')
        password = dict.get('password')
        email = dict.get('email')
        username = dict.get('username')
        Profile.objects.create(email=email , username = username , password = password , profile_pic = pic)
        return response.Response(status=200)
@decorators.api_view(['GET'])
def discussion_api_view(request , pk):
    discussion = Discussion.objects.get(pk = pk)
    if discussion.profile_one == request.user or discussion.profile_two == request.user : 
        return 