from django.urls import path
from .views import *


urlpatterns = [
    path('recent_discussions/' , recent_discussions),
    path('create_profile/' , CreateProfileApiView.as_view())
]