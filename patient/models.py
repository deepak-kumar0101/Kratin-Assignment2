from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.


class patient_details(models.Model):
    patient_id=models.IntegerField()
    patiengt_name=models.CharField(max_length=200)
    patient_age=models.IntegerField()
    address=models.CharField(max_length=300)

class emergency_contact(models.Model):
    h_id=models.CharField(max_length=10)
    hospitals_name=models.CharField(max_length=300)
    h_address=models.CharField(max_length=200)
    h_contactno=models.IntegerField()
    


class health_test_lab(models.Model):
    lab_id=models.CharField(max_length=10)
    lab_name=models.CharField(max_length=200)
    lab_address=models.CharField(max_length=300)
    lab_specialisation=models.CharField(max_length=300)
    las_appo_availability=models.IntegerField()


class medicalstore(models.Model):
    store_name=models.CharField(max_length=300)
    store_address=models.CharField(max_length=200)
    store_contactno=models.IntegerField()

    
