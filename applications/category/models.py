from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.
class Categories(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'