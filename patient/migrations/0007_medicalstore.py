# Generated by Django 5.0.4 on 2024-04-06 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_health_test_lab_alter_emergency_contact_h_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='medicalstore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=300)),
                ('store_address', models.CharField(max_length=200)),
                ('store_contactno', models.IntegerField()),
            ],
        ),
    ]
