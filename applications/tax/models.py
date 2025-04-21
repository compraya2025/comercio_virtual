from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.
class Taxes(TimeStampedModel):
    name = models.CharField(max_length=60,unique=True)
    percentage = models.CharField(max_length=8, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tax'
        verbose_name_plural = 'Taxes'