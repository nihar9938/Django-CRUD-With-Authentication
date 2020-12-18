from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Custom Manager Class 

class UserAccountManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,address,company,password=None):
        if not email:
            raise ValueError('User Must Have an Email Address')

        email=self.normalize_email(email)
        user = self.model(email=email,first_name=first_name,last_name=last_name,address=address,company=company)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,first_name,last_name,address,company,password=None):
        user=self.create_user(email,first_name,last_name,address,company,password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

#Custom User Class
class Manager(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=250,unique=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    address=models.CharField(max_length=150,blank=True)
    company=models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects=UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','company','address']

    def __str__(self):
        return self.email