from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.
class Company(TimeStampedModel):
    name = models.CharField(max_length=80, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'companies'
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'