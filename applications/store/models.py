from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.
class Store(TimeStampedModel):
    name_store = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100, unique=True)
    phone_store = models.IntegerField(max_length=20)
    image_baner = models.CharField(max_length=120, blank=True)
    image_horizontal = models.CharField(max_length=120, blank=True)
    image_vertical = models.CharField(max_length=120, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    #para panel adminstral en el admin
    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'
