# Generated by Django 4.2.6 on 2024-04-05 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='emergency',
            new_name='patient_details',
        ),
    ]
