from django.db import models
from django.contrib.auth.models import BaseUserManager , PermissionsMixin , AbstractBaseUser
# Create your models here.
class ProfileManager(BaseUserManager):
    def create_user(self,email, username , password = None):
        email = self.normalize_email(email)
        user = self.model(email = email , username = username)
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self , email , username = None , password =None) : 
        user = self.create_user(email , username , password)
        user.is_staff = True
        user.save(using = self._db)
        return user
class Profile(AbstractBaseUser , PermissionsMixin) : 
    email = models.EmailField(max_length=255 , unique = True)
    username = models.CharField(max_length=24 , blank=True , null=True)
    profile_pic = models.ImageField(upload_to = 'profile_pics' , blank = True , null = True)
    USERNAME_FIELD = 'email'
    objects = ProfileManager()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    def __str__(self):
        return self.email