# Generated by Django 4.2.6 on 2024-04-05 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_rename_emergency_patient_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='patient_details',
        ),
    ]
