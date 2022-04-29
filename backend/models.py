from django.db import models
from django.db.models.signals import pre_save
from autoslug import AutoSlugField

# Create your models here.
class Joinus(models.Model):
    Fullname = models.CharField(max_length=70)
    Email= models.CharField(max_length=70)
    Contact = models.IntegerField()

Sec = (
    ('L1','L1'),
    ('L2', 'L2'),
    ('L3','L3'),
    ('L4','L4'),
    ('L5','L5'),
)
class Student(models.Model):
    Fullname = models.CharField(max_length=70)
    StdiD =  models.CharField(max_length=70, unique=True)
    Password = AutoSlugField(populate_from='StdiD')
    Amt = models.FloatField()
    Section = models.CharField(max_length=6, choices=Sec, default="L1")
    Address = models.CharField(max_length=70)
    Email = models.EmailField(max_length=50)
    Fathers_name = models.CharField(max_length=70,null=True)
    Contact = models.IntegerField(max_length=10,null=True)

# def gen_pass(sender,instance,*args, **kwargs):
#     if not instance.Password:
#         id=instance.StdiD[-3:]
#         instance.Password = f"Herald{id}"

# pre_save.connect(gen_pass,sender=Student)
