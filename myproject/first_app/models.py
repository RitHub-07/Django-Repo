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

  def __str__(self):
    return self.category_name


class Category_Products(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
  product_name = models.CharField(max_length=100)
  product_description = models.TextField()
  original_price = models.DecimalField(max_digits=10, decimal_places=2)
  selling_price = models.DecimalField(max_digits=10, decimal_places=2)
  product_image = models.ImageField(upload_to="product_image")
  quantity = models.PositiveBigIntegerField(default=1)

  def __str__(self):
    return self.product_name

# class Cart(models.Model):
#   user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='cart')
#   cart = models.CharField(max_length=100, default='cart')
#   created_at = models.DateTimeField(auto_now_add=True)


#   def __str__(self):
#     return f"Cart of {self.user.username} created at {self.created_at}"


# class CartItem(models.Model):
#   cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
#   product = models.ForeignKey(Category_Products, on_delete=models.CASCADE)
#   quantity = models.PositiveIntegerField(default=1)

#   def __str__(self):
#     return f"{self.product.product_name} in {self.cart.user.username}'s cart"

  
class ContactUs(models.Model):
  contact_name = models.CharField(max_length=100)
  contact_email = models.CharField(max_length=100)
  contact_message = models.TextField()




