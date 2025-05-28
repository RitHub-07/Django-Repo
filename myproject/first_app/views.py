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
from django.urls import reverse


# Create your views here.

def base_view(request):
    return render(request,'base.html')


def home_view(request):
    categories = Category.objects.all()
    return render(request,'home.html', {'category_variable':categories})



def about_view(request):
    return render(request, 'about.html')

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
        return redirect('/')  
    return render(request, 'student_update.html', {'student': student})


def student_delete(request, id):
    
    student = get_object_or_404(Student, id = id)
    if request.method == "POST":
         student.delete()

    return redirect('/')


def categories_view(request):
     categories = Category.objects.all()
     return render(request, 'category.html', {'category_variable': categories})

from django.shortcuts import render

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

def saved_address(request):
    return render(request, 'saved_address.html')


@login_required

def edit_profile(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')

        if not first_name or not last_name or not username:
            messages.error(request, 'All fields are required.')
            return redirect('/edit-profile/')

        # Check if username is taken by someone else
        if User.objects.filter(username=username).exclude(id=request.user.id).exists():
            messages.error(request, 'Username already taken.')
            return redirect('/edit-profile/')

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
        return redirect('/my_profile/')

    return render(request, 'edit_profile.html')
