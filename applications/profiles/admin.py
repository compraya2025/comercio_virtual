from django.contrib import admin

from .models import Profile
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','photo_profile','full_name','age_profile','neighborhood','ruc_profile',
                'birth_date',
                'address'
            )
    
    search_fields = ('id','full_name')

    list_per_page = 10  
