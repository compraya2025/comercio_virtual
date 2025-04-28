from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
         model = Product
         fields = (
            'id', 
            'title',
            'brand',
            'description',
            'over_product',
            'code_bar_product',
            'code_lote_product',
            'stock',
            'price_sale',
            'purchase_price',
            'discount_price',
            'promotion',
            'url_image_one_product',
            'url_image_two_product',
            'url_image_three_product',
            'category',
            'tax',
            'store',
            'material_product' ,
            'color', 
            'garantia_product',
            'created',
            'modified', 
         )