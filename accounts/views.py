from django.shortcuts import render
from django.contrib.auth import get_user_model
User=get_user_model()
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
import re

regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


# View Class For New Manager Sign Up

class Signup(APIView):
    permission_classes=(permissions.AllowAny,)

    def post(self,request,format=None):
        data=self.request.data

        firstname=data['first_name']
        lastname=data['last_name']
        email=data['email']
        address=data['address']
        company=data['company']
        password=data['password']
        password2=data['password2']

        if not re.search(regex,email):
            return Response({'error':'Provide Valid Email'})

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'})
            else:
                if len(password) < 6:
                    return Response({'error': 'Password must be at least 6 characters'})
                else:
                    user = User.objects.create_user(email=email,first_name=firstname,last_name=lastname,address=address,company=company,password=password)
                    user.save()
                    return Response({'success': 'User created successfully'})
        else:
            return Response({'error': 'Passwords do not match'})