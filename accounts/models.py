from os import access
from pyexpat import model
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.

class UserManager(BaseUserManager):
    
    def create_user(self, username, email, first_name, last_name, password=None):
        
        if username is None:
            raise TypeError('Username is required')
        if email is None:
            raise TypeError('Email is required')
        if first_name is None:
            raise TypeError('Firstname is required')
        if last_name is None:
            raise TypeError('Lastname is required')
        
        user = self.model(username=username, first_name=first_name, last_name=last_name, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user
        
    def create_superuser(self, username, email, password=None):
        
        if password is None:
            raise TypeError('Password is required')
        
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=250, unique=True, db_index=True)
    email = models.EmailField(max_length=250, unique=True, db_index=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh' : str(refresh),
            'access' : str(refresh.access_token)
        }   
    