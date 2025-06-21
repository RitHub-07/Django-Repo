from django.contrib import admin
from django.urls import path,include
# from .views import home_view
from .views import *
from .views import term_conditions
from .views import privacy_policy


urlpatterns = [
  path('', home_view, name='home'),  
  path('base', base_view, name='base'),  


  path('abouttt/', about_view, name='about'),  
  path('our_vision/', our_vision, name='our_vision'),  
  path('our_Mission/', our_Mission, name='our_Mission'),  
  path('contact/',contact_view,name='contact'),
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

  # path('categories_product/<int:category_id>/',categories_view, name='categories_product'),
  path('products/<int:category_id>/', categories_product, name='categories_product'),
  path('my-orders/', my_orders, name='my_orders'),
  path('cart/', cart_view, name='cart'),
  path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
  path('remove-cart-item/<int:item_id>/', remove_cart_item, name='remove_cart_item'),
  path('checkout/', checkout_view, name='checkout'),
  path('place-order/', place_order, name='place_order'),


  path('increase-quantity/<int:item_id>/', increase_quantity, name='increase_quantity'),
  path('decrease-quantity/<int:item_id>/', decrease_quantity, name='decrease_quantity'),
  path('clear-cart/', clear_cart, name='clear_cart'),

  path('return-policy/', return_policy, name='return_policy'),


  path('wishlist/', wishlist_view, name='wishlist'),
  path('add-to-wishlist/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
  path('remove-wishlist-item/<int:item_id>/', remove_wishlist_item, name='remove_wishlist_item'),
  
  path('emp/create/', employee_add, name='employee_add'),
  path('emp/list/', employee_list, name='employee_list'),
  path('emp/edit/<int:id>/', employee_update, name='employee_edit'),  
  path('emp/delete/<int:id>/', employee_delete, name='employee_delete'),

  path('product/<int:product_id>/', product_detail, name='product_detail'),
  path('order/<int:order_id>/', order_detail_view, name='order_detail'),
  path('order/cancel/<int:order_id>/', cancel_order, name='cancel_order'),

]
