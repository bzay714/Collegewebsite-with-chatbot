# Generated by Django 4.0.1 on 2022-04-11 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_alter_bill_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='Password',
            field=models.SlugField(blank=True),
        ),
    ]
