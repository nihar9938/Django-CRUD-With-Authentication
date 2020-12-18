from django.urls import path
from .views import *

#Url Patterns For Employees
urlpatterns = [
    path('', EmployeeList.as_view()),
    path('create',EmployeeCreate.as_view()),
    path('retrieve/<int:Eid>',EmployeeRetrieve.as_view()),
    path('update/<int:Eid>',EmployeeUpdate.as_view()),
    path('delete/<int:Eid>',EmployeeDelete.as_view())
]