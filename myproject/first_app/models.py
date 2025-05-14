from django.db import models

# Create your models here.

class Student(models.Model):
  student_id = models.IntegerField()
  student_name = models.CharField(max_length=100)
  father_name = models.CharField(max_length=100)
  student_roll = models.IntegerField()



# all models ( tables )  for database 
# this file is responsible for database 