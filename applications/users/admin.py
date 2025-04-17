from django.contrib import admin

# Register your models here.
from .models import User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','last_name','username','email','is_active','is_staff','is_suscription')
    
    search_fields = ('id','name')

    list_per_page = 10  
