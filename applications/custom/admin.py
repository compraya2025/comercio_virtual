from django.contrib import admin

from .models import Custom
# Register your models here.
#admin.site.register(Custom)
@admin.register(Custom)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','profile','created','modified')

    search_fields = ('id','profile')

