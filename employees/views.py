from django.shortcuts import render
from .models import Employee
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from .serializers import EmployeeSerializer
from rest_framework import permissions


# Create your views here.

#Employee List Class
class EmployeeList(ListAPIView):
    queryset=Employee.objects.all().order_by('-Eid')
    serializer_class=EmployeeSerializer

#Create Employee class
class EmployeeCreate(CreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field="Eid"

#Employee Retrieve Class
class EmployeeRetrieve(RetrieveAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field="Eid"

#Employee Update Class
class EmployeeUpdate(UpdateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field="Eid"

#Employee Delete Class
class EmployeeDelete(DestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field="Eid"
