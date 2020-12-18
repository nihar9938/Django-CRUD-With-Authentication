# Django-CRUD-With-Authentication
# Backend Development Using Python(Django Rest Framework)
---
## Steps to Run The Project:
  * System must have python 3.6 or more.
  * Clone the repo `git clone https://github.com/nihar9938/Django-CRUD-With-Authentication`
  * Create virtual environment `py -m venv venv`
  * Activate Virtual Environment `.\venv\Scripts\activate`
  * install requirement.txt `pip install requirement.txt`
  * Go to the directory where manage.py is present.
  * Start the Server`python manage.py runserver`
  
 ## API Endpoints:
 `[Base url:127.0.0.1:8000]`
 #### Signup:
  Api:`http://127.0.0.1:8000/api/signup/{body}`
  Schema:
  ```
  {
    "first_name":"",
    "last_name" :"",
    "email":"",
    "company":"",
    "address":"",
    "password":"",
    "password2":""
}
```
#### Login
  Api:`http://127.0.0.1:8000/api/token/{body}`
  Schema:
  ```
  {
    "email":"",
    "Password":""
   }
  ```
#### Employee Create:
  Api:`http://127.0.0.1:8000/api/{body}`
  Schema:
  ```
    "Eid"="",
    "Firstname"="",
    "Lastname"="",
    "Email"="",
    "Dob"="",
    "Company"="",
    "Address"="",
    "Mobile"="",
    "City"=""
}
```
#### Employee List:
  Api:`http://127.0.0.1:8000/api/`
#### Employee Get:
  api:`http://127.0.0.1:8000/api/{Eid}`
#### Employee Update:
  Api:`http://127.0.0.1:8000/api/{Eid}`
  Schema:
  ```
  {
     "Eid"="",
    "Firstname"="",
    "Lastname"="",
    "Email"="",
    "Dob"="",
    "Company"="",
    "Address"="",
    "Mobile"="",
    "City"=""
}
```
#### Employee Delete:
  Api:`http://127.0.0.1:8000/api/{Eid}`
