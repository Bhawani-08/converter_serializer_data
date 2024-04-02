from django.contrib import admin
from .models import Table1,Table2
# Register your models here.

class Table1Admin(admin.ModelAdmin):
    list_display = ('name','class1')

admin.site.register(Table1,Table1Admin)

class Table2Admin(admin.ModelAdmin):
    list_display = ('sub','roll_no')

admin.site.register(Table2,Table2Admin)

              
