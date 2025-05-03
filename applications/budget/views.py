from rest_framework import viewsets, status
from rest_framework.response import Response

#
from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.utils import timezone
from decimal import Decimal
from .models import Budget, BudgetDetail
from applications.product.models import Product
from .serializers import ProductSerializer, BudgetCreateSerializer, BudgetReadSerializer
# Create your views here.


class BudgetsViewSet(viewsets.ViewSet):

    #
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated,IsAdminUser]
    
    def list(self, request):
        budgets = Budget.objects.prefetch_related('details__product').all()
        serializer = BudgetReadSerializer(budgets, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BudgetCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Crear presupuesto base
        budget = Budget.objects.create(date=timezone.now())

        total = Decimal('000.00')
        incomen = Decimal('000.00')
        detalles = []

        for item in serializer.validated_data['details']:
            try:
                product = Product.objects.get(id=item['product_id'])
            except Product.DoesNotExist:
                return Response({'error': f"Producto ID {item['product_id']} no encontrado"}, status=400)

            quantity = item['quantity']
            price = item['purchase_price']
            subtotal = price * quantity
            ingreso = product.price_sale * quantity  # suponiendo que tiene price_sale

            total += subtotal
            incomen += ingreso

            detalles.append(BudgetDetail(
                budget=budget,
                product=product,
                quantity=quantity,
                purchase_price=price,
                subtotal=subtotal
            ))

        BudgetDetail.objects.bulk_create(detalles)

        # Actualizar totales
        budget.total = total
        budget.incomen = incomen
        budget.save()

        return Response({'message': 'Presupuesto creado exitosamente'}, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        budget = self.get_object()
        serializer = self.get_serializer(budget)
        return Response(serializer.data)
            
            