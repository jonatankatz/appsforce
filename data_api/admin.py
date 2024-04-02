from django.contrib import admin
from .models import User, Department
# Register your models here.

admin.site.register(Department)
admin.site.register(User)
