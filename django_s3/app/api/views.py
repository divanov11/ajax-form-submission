from django.shortcuts import render
from  app.models import *
from django.http import JsonResponse
from . serializers import *

def customers(request):
	customers = Customer.objects.all()
	serializer = CustomerSerializer(customers, many=True)
	return JsonResponse(serializer.data, safe=False)