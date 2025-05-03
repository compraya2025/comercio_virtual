from django.db import models
from decimal import Decimal

from applications.product.models import Product

# Create your models here.

class Budget(models.Model):
    date  = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    incomen = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    def __str__(self):
        return f"Presupuesto #{self.pk} - {self.date.date()}"

class BudgetDetail(models.Model):
    budget         = models.ForeignKey(Budget, related_name='details', on_delete=models.CASCADE)
    product        = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity       = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal       = models.DecimalField(max_digits=12, decimal_places=2)