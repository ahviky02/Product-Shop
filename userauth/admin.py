from django.contrib import admin
from .models import CustomUser, AdminUser

admin.site.register(CustomUser)
admin.site.register(AdminUser)