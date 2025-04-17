from django.db import models
from model_utils.models import TimeStampedModel
from applications.profiles.models import Profile

# Create your models here.
class Custom(TimeStampedModel):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    
    #para panel adminstral en el admin
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'