import django_filters

from .models import Taxes

class TaxFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name='id', lookup_expr='exact')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model =  Taxes
        fields = ['id','name']