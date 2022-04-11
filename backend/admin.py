from django.contrib import admin
from .models import *



# Register your models here.
@admin.register(Joinus)
class AdminJoinus(admin.ModelAdmin):
    list_display = ['id','Fullname','Email','Contact']

@admin.register(Student)
class AdminBill(admin.ModelAdmin):
    list_display = ['Fullname','StdiD','Password','Amt','Section','Address','Email']

