from django.contrib import admin
from .models import crop, location

# Register your models here.


admin.site.register(location)
admin.site.register(crop)