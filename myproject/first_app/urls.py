from django.contrib import admin
from django.urls import path,include
# from .views import home_view
from .views import *

urlpatterns = [
  path('', home_view, name='home'),  

  path('abouttt', about_view, name='about'),  
  path('contact',contact_view,name='contact'),
  path("register/", register_page , name="register"),
  path("student/create/", student_submit, name= "student_submit"),
  path("student/list",student_list_view,name = "student_list_view"),
  path("login",login_page,name="login"),
  path('logout',logout_page, name="logout_page"),
  path('student/edit/<int:id>/', student_edit, name='student_edit'),
  path("student/delete/<int:id>/", student_delete, name="student_delete"),
  path("categories/",categories_view,name="categories_view")


]
