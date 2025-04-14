from django.db import models
from django.conf import settings
from applications.users.models import User
from model_utils.models import TimeStampedModel

# Create your models here.
class Profile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    photo_profile = models.ImageField(upload_to="img/profile/", blank=True)
    full_name = models.CharField(max_length=80,unique=True)
    age_profile = models.IntegerField(max_length=100)
    neighborhood= models.CharField(max_length=100)
    ruc_profile = models.CharField(max_length=10, unique=True)
    phone_profile = models.CharField(max_length=15,unique=True, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
       return f"Perfil de {self.age_profile}" 