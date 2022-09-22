from django.db import models
from profiles.models import Profile
# Create your models here.
class DiscussionManager(models.Manager):
    def create_discussion(self , profile , profile_two):
        if profile.id > profile_two.id : 
            if Discussion.objects.filter(profile_one = profile_two , profile_two = profile):
                raise ValueError("disccussion already exists")
            else : 
                discussion= self.model(profile_one = profile_two , profile_two = profile)
                discussion.save(using = self._db)
        elif profile.id < profile_two.id : 
            if Discussion.objects.filter(profile_one = profile , profile_two = profile_two):
                raise ValueError("disccussion already exists")
            else : 
                discussion= self.model(profile_one = profile , profile_two = profile_two)
                discussion.save(using = self._db)
        else : 
            raise ValueError("discussion has to have two different profiles")
        return discussion
class Discussion(models.Model):
    profile_one = models.ForeignKey(Profile , on_delete=models.CASCADE , related_name='dis')
    profile_two = models.ForeignKey(Profile , on_delete=models.CASCADE)