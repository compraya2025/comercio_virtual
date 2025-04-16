from django.db import models
#
from model_utils.models import TimeStampedModel
from applications.country.models import Country

# Create your models here.
class Departments(TimeStampedModel):
    name = models.CharField('Nombre departamento',unique=True,max_length=60)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'