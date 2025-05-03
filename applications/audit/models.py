from django.db import models
#
from model_utils.models import TimeStampedModel
from applications.product.models import Product

from applications.users.models import User


class Audit(TimeStampedModel):
    producto = models.ForeignKey(Product, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    accion = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)      


