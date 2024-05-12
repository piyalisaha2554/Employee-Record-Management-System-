from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(EmployeeDetail)
admin.site.register(NonTeachingEmployee)
admin.site.register(TeachingEmployee)
