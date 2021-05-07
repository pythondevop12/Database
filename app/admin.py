from django.contrib import admin
from .models import Mydb

@admin.register(Mydb)
class MydbAdmin(admin.ModelAdmin):
 list_display = ['id','name','age','address','mobile']
