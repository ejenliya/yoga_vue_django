from django.contrib import admin

from .models import User,Admin
# Register your models here.

admin.site.register(Admin)
admin.site.register(User)
