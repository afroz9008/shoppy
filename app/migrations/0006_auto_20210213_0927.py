# Generated by Django 3.1.5 on 2021-02-13 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_specialitems'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specialitems',
            old_name='active',
            new_name='Active',
        ),
    ]