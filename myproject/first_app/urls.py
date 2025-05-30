from django.contrib import admin
from django.urls import path,include
# from .views import home_view
from .views import *
from .views import term_conditions
from .views import privacy_policy


urlpatterns = [
  path('', base_view, name='base'),  
  path('flipkart', home_view, name='home'),  


  path('abouttt', about_view, name='about'),  
  path('contact',contact_view,name='contact'),
  path("register/", register_page , name="register"),
  path("student/create/", student_submit, name= "student_submit"),
  path("student/list",student_list_view,name = "student_list_view"),
  path("login",login_page,name="login"),
  path('logout',logout_page, name="logout_page"),

  path('student/edit/<int:id>/', student_edit, name='student_edit'),
  
  path("student/delete/<int:id>/", student_delete, name="student_delete"),
  path("my_profile/",profile_view,name="profile_view"),
  path('saved_address', saved_address, name='saved_address'),
  path("edit_profile/",edit_profile, name="edit_profile"),
  path('term-and-conditions/', term_conditions, name='term_conditions'),
  path('privacy-policy/', privacy_policy, name='privacy_policy'),
  path("categories/",categories_view,name="categories_view"),

  path('products/<int:category_id>/', categories_product, name='categories_product'),
  path('my-orders/', my_orders, name='my_orders'),
  path('cart/', cart_view, name='cart'),
  path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
]
