# AeraTek CMS
***
AeraTek CMS Administration for website.

## Versions
1. [AeraTekBackend] (v.1.0.0) [Date] (22-Oct-2023)

## Table of Contents
1. [Technologies](#Technologies)
2. [Installation](#Installation)
3. [Collaboration](#collaboration)
4. [FAQs](#FAQs)

## Technologies
1. [python](https://www.python.org/): 3.11.6
2. [Django](https://www.djangoproject.com/):4.2.6
3. [Django RestFramework](https://www.django-rest-framework.org/):3.14.0

## Installation
***
To install and run the AeraTek CMS via local. 
```
$ git clone https://example.com
$ cd ../aeratekBackend
$ pip install virtualenv
$ python3 -m venv venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
$ python3 manage.py migrate
$ python3 manage.py runserver 127.0.0.1:8000

***
To install and run the AeraTek CMS via Docker. 
```
$ docker build -t aeratekbackend .
$ docker run -d --name aeratekbackend aeratekbackend

## Api Endpoints

***
About Us
```
About Us Section
$ http://{backend_url}/api/aboutUs/

***
Banners
```
Banners Section
$ http://{backend_url}/api/banners/

***
Services
```
Cards Info Services
$ http://{backend_url}/api/services/

Services Info Detail
$ http://{backend_url}/api/ServiceDetailView/{primary_key}/

***
Projects
```
Cards Info Projects
$ http://{backend_url}/api/projects/

Projects Info Detail
$ http://{backend_url}/api/ProjectsDetailView/{primary_key}/

***
News
```
Cards Info News
$ http://{backend_url}/api/news/

News Info Detail
$ http://{backend_url}/api/NewsDetailView/{primary_key}/

***
Contact
```
List Contact Messages
$ http://{backend_url}/api/contact/
```

***
Maps
List Maps
$ http://{{Backend_url}}/api/maps/
```
***
POST New Contact Message
@POST
$ http://{backend_url}/api/contact/
```

## Collaboration
***
Collaborators in this project.
> Rolando Antonio Aguilar Mejia github:rolandoaamejia
> Rolando Mejia Medina github:rolando-mejia
```
## FAQs
***
A list of frequently asked questions
1. **How to Initialize Docker**
You have to install docker, and via cmd run the commands. 
2. **I have trouble with the virtual enviroment**
To run the virtualenv or create you have to use the command for your OS