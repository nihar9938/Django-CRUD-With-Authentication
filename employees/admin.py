from django.contrib import admin
from .models import *

# Register Models For Admin Panel

class Employeeadmin(admin.ModelAdmin):
    list_display=["Eid","Firstname","Lastname","Email","Mobile","City"]

admin.site.register(Employee,Employeeadmin)
