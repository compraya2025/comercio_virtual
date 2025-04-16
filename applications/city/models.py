from django.db import models
#
from django.db import models
from model_utils.models import TimeStampedModel
#
from applications.department.models import Departments

# Create your models here.
class Cities(TimeStampedModel):
    name = models.CharField('Nombre ciudad',unique=True,max_length=60)
    department = models.ForeignKey(Departments, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'