from django.db import models
from applications.category.models import Categories
from applications.tax.models import Taxes
from applications.store.models import Store

from model_utils.models import TimeStampedModel

# Create your models here.
class Product(TimeStampedModel):
    
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, blank=True)
    description = models.TextField(max_length=256,null=True)
    over_product = models.TextField(blank=True)
    code_bar_product = models.CharField(max_length=255)
    code_lote_product = models.CharField(max_length=255,blank=True)
    stock = models.DecimalField(max_digits=10, decimal_places=0)
    price_sale = models.DecimalField(max_digits=10, decimal_places=3)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=3)
    discount_price = models.DecimalField(max_digits=10, decimal_places=3)
    promotion = models.BooleanField(default=False)
    url_image_one_product = models.ImageField(upload_to='img/product/', blank=True)
    url_image_two_product = models.ImageField(upload_to='img/product/', blank=True)
    url_image_three_product = models.ImageField(upload_to='img/product/', blank=True)
    category = models.ForeignKey(Categories, on_delete=models.PROTECT)
    tax = models.ForeignKey(Taxes, on_delete=models.PROTECT)
    store = models.ForeignKey(Store, on_delete=models.PROTECT)
    material_product = models.CharField(max_length=60, null=True)
    color = models.CharField(max_length=60, null=True)
    garantia_product = models.CharField(max_length=80, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'