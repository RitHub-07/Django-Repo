from django.db import models

# Create your models here.

class Student(models.Model):
  student_image = models.ImageField(upload_to='student_images')
  registration_id = models.IntegerField()
  student_name = models.CharField(max_length=100)
  father_name = models.CharField(max_length=100)
  student_roll = models.IntegerField()


class Category(models.Model):
  category_name = models.CharField(max_length=100)
  category_description = models.TextField()
  category_image = models.ImageField(upload_to="category_image")
  
class ContactUs(models.Model):
  contact_name = models.CharField(max_length=100)
  contact_email = models.CharField(max_length=100)
  contact_message = models.TextField()

# all models ( tables )  for database 
# this file is responsible for database 
