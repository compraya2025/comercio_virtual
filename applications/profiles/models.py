from django.db import models
from django.conf import settings
from applications.users.models import User
from model_utils.models import TimeStampedModel
#
from applications.country.models import Country
from applications.department.models import Departments
from applications.city.models import Cities

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
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    department = models.ForeignKey(Departments, on_delete=models.PROTECT)
    city = models.ForeignKey(Cities, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
    
    def __str__(self):
       return f"Perfil de {self.age_profile}" 