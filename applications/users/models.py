from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,name, last_name,username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio.')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            last_name=last_name,
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
       
        return user

    """ def create_superuser(self, email, name, last_name, username, password=None,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True) 

        return self.create_user(email, name, last_name, username, password, **extra_fields)"""
    
    def create_superuser(self, email, name, last_name, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(
            name=name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
            **extra_fields
        )
         
    
class User(AbstractBaseUser, PermissionsMixin,TimeStampedModel):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    username = models.CharField(max_length=80)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_suscription = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','name','last_name']

    def __str__(self):
        return self.email
