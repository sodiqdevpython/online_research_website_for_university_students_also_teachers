from django.contrib import admin
from .models import CustomUser

class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'created_date')

@admin.register(CustomUser)
class AdminUserView(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','date_joined']
    search_fields = ['email','first_name','last_name']