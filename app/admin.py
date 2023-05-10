from django.contrib import admin
from app.models import Employee
# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display=['name','email','password']
    

admin.site.register(Employee,EmpAdmin)   