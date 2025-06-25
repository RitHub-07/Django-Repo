from django.shortcuts import render
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.http import HttpResponse
from .models import *
# from .models import Student 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout 
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import os
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect
# from django.urls import CartItem
# from .models import Product


# Create your views here.

def base_view(request):
    return render(request,'base.html')


def home_view(request):
    # Main categories to display (change number/order anytime)
    categories = Category.objects.all()[:6]  # Show 6 categories
    
    # Top deals section (filter products marked as deals)
    top_deals = Category_Products.objects.filter(is_top_deal=True)[:4]  # Show 4 deals
    
    # Main products section (shows all products by default)
    products = Category_Products.objects.all().order_by('-id')[:8]  # Show 8 newest
    
    return render(request, 'home.html', {
        'category_variable': categories,  # Kept same name for template compatibility
        'top_deals': top_deals,          # For deals banner
        'all_products': products,        # Kept same name for template compatibility
    })

def about_view(request):
    return render(request, 'about.html')


def our_vision(request):
    return render(request, 'ourVision.html')


def our_Mission(request):
    return render(request, 'ourMission.html')


def contact_view(request):
    return render(request,'contact.html')


def register_page(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Basic field validation
        if not first_name or not last_name or not username or not password:
            messages.error(request, 'All fields are required.')
            return redirect('/register/')
        

        # Password length check
        if len(password) < 6:
            messages.error(request, 'Password must be at least 6 characters long.')
            return redirect('/register/')
        
        


        # Username check
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return redirect('/register/')

        # Create user
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()

        messages.success(request, 'Account created successfully.')
        return redirect('/')

    return render(request, 'register.html')


def login_page(request):

      if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')



            if not User.objects.filter(username= username).exists():
                  messages.error(request, 'Invalid Username')
                  return redirect('/login/')

            user = authenticate(username = username,password=password)      


            if user is None:
                  messages.error(request, 'Invalid Password') 
                  return redirect('/login')

            else:
                  login(request, user)    
                  return redirect('/')  


      return render(request,'login.html')


def logout_page(request):
    logout(request)
    return redirect('/login')  # Redirect to login page after logout
     

def student_submit(request):
    if request.method == "POST":
        registration_id = request.POST.get('registration_id')
        student_name = request.POST.get('student_name')
        father_name = request.POST.get('father_name')
        student_roll = request.POST.get('student_roll')

        student_image = request.FILES.get('student_image')

        std = Student.objects.create(
            registration_id = registration_id,
            student_name = student_name,
            father_name = father_name,
            student_roll = student_roll,
            student_image = student_image
        )

        std.save()

        messages.success(request, 'student data submitted successfully')
        return redirect('/')
    
    return render(request, 'student_form.html')


def student_list_view(request):
    std = Student.objects.all()
    return render(request, 'student_list.html', {'student_data':std})


def student_edit(request, id):
    
    student = get_object_or_404(Student, id = id)

    if request.method == "POST":
        student.registration_id = request.POST.get('registration_id')
        student.student_name = request.POST.get('student_name')
        student.father_name = request.POST.get('father_name')
        student.student_roll = request.POST.get('student_roll')

        if request.FILES.get('student_image'):
             student.student_image = request.FILES.get('student_image')
             
        student.save()
        messages.success(request, 'student data updated successfully')
        return redirect('/base')  
    return render(request, 'student_update.html', {'student': student})


def student_delete(request, id):
    
    student = get_object_or_404(Student, id = id)
    if request.method == "POST":
         student.delete()

    return redirect('/')


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'emp_list.html', {'employees': employees})


def employee_add(request):
    if request.method == 'POST':
        emp_id = request.POST['emp_id']
        emp_first_name = request.POST['emp_first_name']
        emp_last_name = request.POST['emp_last_name']
        emp_city = request.POST['emp_city']
        emp_name = request.POST['emp_name']
        emp_salary = request.POST['emp_salary']

        Employee.objects.create(
            emp_id=emp_id,
            emp_first_name=emp_first_name,
            emp_last_name=emp_last_name,
            emp_city=emp_city,
            emp_name=emp_name,
            emp_salary=emp_salary,
        )
        return redirect('employee_list')
    return render(request, 'emp_form.html')

def employee_update(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.emp_id = request.POST['emp_id']
        employee.emp_first_name = request.POST['emp_first_name']
        employee.emp_last_name = request.POST['emp_last_name']
        employee.emp_city = request.POST['emp_city']
        employee.emp_name = request.POST['emp_name']
        employee.emp_salary = request.POST['emp_salary']
        employee.save()
        return redirect('employee_list')
    return render(request, 'emp_update.html', {'employee': employee})

def employee_delete(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    # return redirect('employee_list')



def term_conditions(request):
    return render(request, 'term_conditions.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')



def contact_view(request):
    if request.method == "POST":
         contact_name = request.POST.get('contact_name')
         contact_email = request.POST.get('contact_email')
         contact_message = request.POST.get('contact_message')


         contact = ContactUs.objects.create(
              contact_name = contact_name,
              contact_email = contact_email,
              contact_message = contact_message
         )

         contact.save()

         messages.success(request, 'Contact us form  submitted successfully')
         return redirect('/')

    return render(request,'contact.html')


def profile_view(request):
     return render(request, 'my_profile.html')

def edit_profile(request):
     return render(request, 'edit_profile.html')


@login_required
def saved_address(request):
    orders = Order.objects.filter(user=request.user)
    addresses = []
    seen = set()

    for order in orders:
        key = (order.name, order.email, order.phone, order.address, order.city, order.pincode)

        if key not in seen:
            seen.add(key)  # Mark this address as seen
            addresses.append({
                'name': order.name,
                'email': order.email,
                'phone': order.phone,
                'address': order.address,
                'city': order.city,
                'pincode': order.pincode
            })

    return render(request, 'saved_address.html', {'addresses': addresses})


@login_required

def edit_profile(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')

        if not first_name or not last_name or not username:
            messages.error(request, 'All fields are required.')
            return redirect('edit_profile')

        # Check if username is taken by someone else
        if User.objects.filter(username=username).exclude(id=request.user.id).exists():
            messages.error(request, 'Username already taken.')
            return redirect('edit_profile.html')

        # Update the user info

        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.save()

        # request.user.first_name = first_name
        # request.user.last_name = last_name
        # request.user.username = username
        # request.user.save()

        messages.success(request, 'Profile updated successfully.')
        return redirect('profile_view')

    return render(request, 'edit_profile.html')



def categories_view(request):
     categories = Category.objects.all()
     return render(request, 'category.html', {'category_variable': categories})

def categories_product(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    
    # products  = Category_Products.objects.all()
    products = Category_Products.objects.filter(category=category)


    return render(request, 'categories_product.html', {'products_variable': products, 'category_variable': category})


def cart_view(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please login to view your cart")
        return redirect('login')  # Adjust to your login URL
    
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.select_related('product')
    
    grand_total = sum(item.product.selling_price * item.quantity for item in cart_items)
    delivery_threshold = 500
    amount_needed = max(0, delivery_threshold - grand_total)

    context = {
        'cart_items': cart_items,
        'grand_total': grand_total,
        'amount_needed': amount_needed,
        'qualifies_for_free_delivery': grand_total >= delivery_threshold,
    }
    return render(request, 'cart.html', context)

def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        messages.error(request, "Please login to add items to cart")
        return redirect('login')
    
    product = get_object_or_404(Category_Products, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity > product.quantity:
        messages.error(request, 'Insufficient stock available')
        return redirect('categories_product', category_id=product.category.id)
    
    cart, _ = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(product=product, cart=cart)
    
    if created:
        item.quantity = quantity
    else:
        item.quantity += quantity
    
    item.save()
    messages.success(request, f'{product.product_name} added to cart')
    return redirect('cart')


def remove_cart_item(request, item_id):
    if not request.user.is_authenticated:
        messages.error(request, "Please login to manage cart")
        return redirect('login')
    
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    messages.success(request, 'Item removed from cart')
    return redirect('cart')

def increase_quantity(request, item_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    
    if item.quantity >= item.product.quantity:
        messages.error(request, f"Only {item.product.quantity} available in stock")
    else:
        item.quantity += 1
        item.save()
    
    return redirect('cart')

def decrease_quantity(request, item_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    
    return redirect('cart')

def clear_cart(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please login to manage cart")
        return redirect('login')
    
    cart = get_object_or_404(Cart, user=request.user)
    cart.items.all().delete()
    messages.success(request, "All items removed from cart")
    return redirect('cart')


def return_policy(request):
    return render(request, 'return_policy.html')


def wishlist_view(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist_items = wishlist.items.select_related('product')
    
    context = {
        'wishlist_items': wishlist_items,
        'wishlist': wishlist,
        }

    return render(request, 'wish_list.html', context)


def add_to_wishlist(request,product_id):
    product = get_object_or_404(Category_Products, id = product_id)
    quantity = int(request.POST.get('quantity', 1))

    
    # get or create cart for user 
    wishlist , created = Wishlist.objects.get_or_create(user=request.user)

    # get or create CartItem 

    wishlistItem, created = WishlistItem.objects.get_or_create(product=product, wishlist=wishlist)


    wishlistItem.save()

    messages.success(request, f'{product.product_name} added to wishlist successfully.')
    return redirect('wishlist')


def remove_wishlist_item(request, item_id):
    wishlist_item = get_object_or_404(WishlistItem, id=item_id, wishlist__user=request.user)
    wishlist_item.delete()

    messages.success(request, 'Item removed from wishlist successfully.')
    return redirect('wishlist')

# def wishlisht_all_remove(request):
#     wishlist = get_object_or_404(WishlistItem, wishlist_user=request)
#     wishlist.items.all().delete()
#     messages.success(request, "All items removed from Wishlist")
#     return redirect('wishlist')




def product_detail(request, product_id):
    product = get_object_or_404(Category_Products, id=product_id)
    
    # Calculate discount percentage if there's an original price
    if hasattr(product, 'get_discount_percentage'):
        discount = product.get_discount_percentage()
    else:
        discount = None
    
    context = {
        'product': product,
        'discount': discount,
    }
    return render(request, 'products_detail_page.html', context)


# def place_order(request):
#     if not request.user.is_authenticated:
#         messages.error(request, "Please login to place an order")
#         return redirect('login')

#     cart = get_object_or_404(Cart, user=request.user)
#     cart_items = cart.items.select_related('product')

#     if not cart_items.exists():
#         messages.error(request, "Your cart is empty")
#         return redirect('cart')

#     total_amount = sum(item.product.selling_price * item.quantity for item in cart_items)

#     order = Order.objects.create(user=request.user, total_amount=total_amount)

#     for item in cart_items:
#         # Create order item
#         OrderItem.objects.create(
#             order=order,
#             product=item.product,
#             quantity=item.quantity,
#             price=item.product.selling_price
#         )

#         # Update product quantity
#         item.product.quantity -= item.quantity
#         item.product.save()

#     # Clear cart
#     cart.items.all().delete()

#     messages.success(request, "Order placed successfully!")
#     return redirect('my_orders')



def place_order(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please login to place an order")
        return redirect('login')

    if request.method == "POST":
        cart = get_object_or_404(Cart, user=request.user)
        cart_items = cart.items.select_related('product')

        if not cart_items.exists():
            messages.error(request, "Your cart is empty")
            return redirect('cart')

        # Get form data
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        name = request.POST.get('name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        payment_method = request.POST.get('payment')

        # Calculate total
        total_amount = sum(item.product.selling_price * item.quantity for item in cart_items)

        # Create Order
        order = Order.objects.create(
            user=request.user,
            email=email,
            phone=phone,
            name=name,
            address=address,
            city=city,
            pincode=pincode,
            payment_method=payment_method,
            total_amount=total_amount
        )

        # Create Order Items
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.selling_price
            )

            # Update stock
            item.product.quantity -= item.quantity
            item.product.save()

        # Clear cart
        cart.items.all().delete()

        messages.success(request, "Order placed successfully!")
        return redirect('home')

    # fallback if accessed via GET
    return redirect('checkout')


def checkout_view(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please login to checkout")
        return redirect('login')
    
    cart = get_object_or_404(Cart, user=request.user)
    if not cart.items.exists():
        messages.error(request, "Your cart is empty")
        return redirect('cart')

    cart_items = cart.items.select_related('product')
    grand_total = sum(item.product.selling_price * item.quantity for item in cart_items)

    return render(request, 'check_out.html', {
        'cart_items': cart_items,
        'grand_total': grand_total
    })






# def my_orders(request):
#     if not request.user.is_authenticated:
#         messages.error(request, "Please login to view orders")
#         return redirect('login')

#     orders = Order.objects.filter(user=request.user).order_by('-created_at')
#     return render(request, 'my_orders.html', {'orders': orders})


from django.utils.dateparse import parse_date
from datetime import datetime

def my_orders(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please login to view orders")
        return redirect('login')

    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')
    search_query = request.GET.get('search', '')

    if from_date:
        orders = orders.filter(created_at__date__gte=parse_date(from_date))
    if to_date:
        orders = orders.filter(created_at__date__lte=parse_date(to_date))
    if search_query:
        orders = orders.filter(items__product__product_name__icontains=search_query).distinct()

    return render(request, 'my_orders.html', {
        'orders': orders,
        'search_query': search_query,})

    # return render(request, 'my_orders.html', {'orders': orders})


def order_detail_view(request, order_id):
    if not request.user.is_authenticated:
        messages.error(request, "Please login to view your orders")
        return redirect('login')

    try:
        order = Order.objects.get(id=order_id, user=request.user)
        return render(request, 'order_page_details.html', {'order': order})
    except Order.DoesNotExist:
        messages.error(request, "Order not found or you don't have permission to view this order")
        return redirect('my_orders')
    
def cancel_order(request, order_id):
    if not request.user.is_authenticated:
        messages.error(request, "Please login to cancel orders")
        return redirect('login')

    try:
        order = Order.objects.get(id=order_id, user=request.user)
        if order.status not in ['Cancelled', 'Delivered']:
            order.status = 'Cancelled'
            order.save()
            messages.success(request, "Order has been cancelled successfully")
        else:
            messages.error(request, "This order cannot be cancelled")
    except Order.DoesNotExist:
        messages.error(request, "Order not found")

    return redirect('order_detail', order_id=order_id)