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
# Create your views here.

def home_view(request):
    return render(request,'base.html')

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
        # if not first_name or not last_name or not username or not password:
        #     messages.error(request, 'All fields are required.')
        #     return redirect('/register/')
        

        # # Password length check
        # if len(password) < 6:
        #     messages.error(request, 'Password must be at least 6 characters long.')
        #     return redirect('/register/')
        


        # # Username check
        # if User.objects.filter(username=username).exists():
        #     messages.error(request, 'Username already taken.')
        #     return redirect('/register/')

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



def student_submit(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        student_name = request.POST.get('student_name')
        father_name = request.POST.get('father_name')
        student_roll = request.POST.get('student_roll')

        std = Student.objects.create(
            student_id = student_id,
            student_name = student_name,
            father_name = father_name,
            student_roll = student_roll
        )

        std.save()

        messages.success(request, 'student data submitted successfully')
        return redirect('/')
    
    return render(request, 'student_form.html')


