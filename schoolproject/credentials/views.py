from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . models import details


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'new.html')
        else:
            messages.info(request, "invalid credentials")
            return redirect(request, 'login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save();
                return redirect('login')

        else:
            messages.info(request, "password not matching")
            return redirect('register')

        return redirect('/')

    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def add(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        age = request.POST['age']
        dob = request.POST['dob']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        gender = request.POST['gender']
        address = request.POST['address']
        department = request.POST['department']
        course = request.POST['course']

        detail = details(fullname=fullname, age=age, dob=dob, phone_number=phone_number, email=email, gender=gender,
                         address=address, department=department, course=course)
        detail.save()
        messages.info(request, "your order confirmed")

    return render(request, 'new.html')


