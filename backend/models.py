from django.db import models

# Create your models here.
class Joinus(models.Model):
    Fullname = models.CharField(max_length=70)
    Email= models.CharField(max_length=70)
    Contact = models.IntegerField()

class Bill(models.Model):
    Fullname = models.CharField(max_length=70)
    StdiD =  models.CharField(max_length=70, primary_key=True)
    Amt = models.FloatField(null=True)

class Teacher(models.Model):
    img = models.FileField(upload_to="media/")
    Fullname =  models.CharField(max_length=70)
    Expertise =  models.CharField(max_length=70)
    Exp =  models.CharField(max_length=70)
    