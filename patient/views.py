from random import randint
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

from patient.models import emergency_contact, health_test_lab, medicalstore, patient_details

# Create your views here.

def regustration(request):
    def otp(digit):
        list=[]
        for i in range(digit):
            list.append(str(randint(0,9)))
        return "".join(list)

    patient=patient_details(patient_id="EL"+otp(4),patiengt_name=request.GET.get('pname'),patient_age=request.GET.get('page'),address=request.GET.get("paddress"))
    patient.save()
    return JsonResponse("Registration succefully",safe=False)

def emergency(request):
    data=patient_details.objects.filter(patient_id=request.GET.get("pid"))
    p_add=(data[0].address)
    data1=emergency_contact.objects.filter(h_address=p_add)
    if len(data1)==0:
        d={"Hospital not avalble in":p_add}
        return JsonResponse(d)
    d={"Hospital_name":data1[0].hospitals_name,"Status":"Arriving soon","Contactno":data1[0].h_contactno}
    return JsonResponse(d)



def lab_inquiry(request):
    lab_specialisation=request.GET.get("lsep")
    data=patient_details.objects.filter(patient_id=request.GET.get("pid"))
    p_add=(data[0].address)
    data1=health_test_lab.objects.filter(Q(lab_address=p_add) & Q(lab_specialisation=lab_specialisation))
    if len(data1)==0:
        d={"Heath checkup lab not avalble in":p_add}
        return JsonResponse(d)
    elif data1[0].las_appo_availability==0:
        return JsonResponse("Appointment not available",safe=False)
    d={"Lab_name":data1[0].lab_name,"Status":"Welcome to "+data1[0].lab_name}
    return JsonResponse(d)


def medical_store(request):
    data=patient_details.objects.filter(patient_id=request.GET.get("pid"))
    p_add=(data[0].address)
    data1=medicalstore .objects.filter(store_address=p_add)
    if len(data1)==0:
        d={"Hospital not avalble in":p_add}
        return JsonResponse(d)
    d={"Hospital_name":data1[0].store_name,"Contactno":data1[0].store_contactno}
    return JsonResponse(d)
    