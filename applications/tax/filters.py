import django_filters

from .models import Taxes

class TaxFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model =  Taxes
        fields = {
            'name':['exact', 'contains'],
            'id':['exact']
        }