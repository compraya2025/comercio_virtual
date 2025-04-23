import django_filters

from applications.store.models import Store

class StoreFilters(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name='id', lookup_expr='exact')
    name_store = django_filters.CharFilter(field_name='name_store', lookup_expr='icontains')
    phone_store = django_filters.CharFilter(field_name='phone_store', lookup_expr='exact')
    class Meta:
        model = Store
        fields = ['id','name_store','phone_store']