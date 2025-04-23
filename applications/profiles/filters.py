import django_filters

from applications.profiles.models import Profile

class ProfileFilters(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name='id', lookup_expr='exact')
    full_name =  django_filters.CharFilter(field_name='full_name', lookup_expr='icontains')
    ruc_profile =  django_filters.CharFilter(field_name='ruc_profile', lookup_expr='icontains')
    class Meta:
        model = Profile
        fields = ['id','full_name','ruc_profile']
        