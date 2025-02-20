from django.contrib import admin

# Register your models here.
from .models import CustomUser, Notes

admin.site.register(CustomUser)
admin.site.register(Notes)
