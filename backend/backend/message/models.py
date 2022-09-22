from django.db import models
from profiles.models import Profile
from discussion.models import Discussion
# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(Profile , on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    sent_on = models.DateTimeField(auto_now_add=True)
    discussion = models.ForeignKey(Discussion , on_delete=models.CASCADE)