# Generated by Django 4.0.1 on 2022-04-29 16:44

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_student_contact_student_fathers_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Password',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='StdiD'),
        ),
    ]
