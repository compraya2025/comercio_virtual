from decimal import Decimal
from rest_framework import serializers
from .models import  Budget, BudgetDetail
from applications.product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','title','price_sale','purchase_price')

    
class BudgetDetailSerializers(serializers.Serializer):
    pk = serializers.IntegerField()
    quantity = serializers.DecimalField(max_digits=10, decimal_places=2)
    purchase_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2)
    product = ProductSerializer(many=True)

class BudgtSerializers(serializers.Serializer):
    date = serializers.DateField()
    total = serializers.DecimalField(max_digits=10, decimal_places=2)
    incomen = serializers.DecimalField(max_digits=10, decimal_places=2)


class BudgetDetailSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    purchase_price = serializers.DecimalField(max_digits=10, decimal_places=2)

class BudgetCreateSerializer(serializers.Serializer):
    details = BudgetDetailSerializer(many=True)

class BudgetDetailReadSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = BudgetDetail
        fields = ['product', 'quantity', 'purchase_price', 'subtotal']

class BudgetReadSerializer(serializers.ModelSerializer):
    details = BudgetDetailReadSerializer(many=True, read_only=True)

    class Meta:
        model = Budget
        fields = ['id', 'date', 'total', 'incomen', 'details']
    
