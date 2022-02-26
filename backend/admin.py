from django.contrib import admin
from .models import Joinus, Bill, Teacher



# Register your models here.
@admin.register(Joinus)
class AdminJoinus(admin.ModelAdmin):
    list_display = ['id','Fullname','Email','Contact']

@admin.register(Bill)
class AdminBill(admin.ModelAdmin):
    list_display = ['Fullname','StdiD','Amt']

@admin.register(Teacher)
class AdminTeacher(admin.ModelAdmin):
    list_display = ['img','Fullname','Expertise','Exp']