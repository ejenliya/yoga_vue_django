from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Day)
admin.site.register(Sex)
admin.site.register(Level)
admin.site.register(Trouble)
admin.site.register(Workout)
