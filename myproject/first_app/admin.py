from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Student)
admin.site.register(Category)
admin.site.register(ContactUs)
admin.site.register(Category_Products)

admin.site.register(Cart)
admin.site.register(CartItem)

# this file is useful for admin panel 