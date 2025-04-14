from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.
class Country(TimeStampedModel):
    name = models.CharField('Nombre pais',unique=True,max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    
    #para panel adminstral en el admin
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'