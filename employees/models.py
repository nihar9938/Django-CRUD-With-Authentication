from django.db import models

# Model For Employees

class Employee(models.Model):
    Eid=models.IntegerField()
    Firstname=models.CharField(max_length=150)
    Lastname=models.CharField(max_length=150)
    Email=models.EmailField(max_length=255)
    Dob=models.DateField()
    Company=models.CharField(max_length=150)
    Address=models.CharField(max_length=200)
    Mobile=models.IntegerField()
    City=models.CharField(max_length=150)

    def __str__(self):
        return self.Firstname