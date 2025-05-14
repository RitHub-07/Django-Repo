from django.contrib import admin
from django.urls import path,include
# from .views import home_view
from .views import *

urlpatterns = [
  path('', home_view, name='home'),  

  path('abouttt', about_view, name='about'),  
  path('contact',contact_view,name='contact'),
  path("register/", register_page , name="register"),
  path("student/create/", student_submit, name= "student_submit")

]
