from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
# Create your views here.
def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def register_process(request):
    errors = User.objects.register_validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    age = request.POST['age']
    email = request.POST['email']
    password = request.POST['password']
    hash_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    User.objects.create(firstname=firstname, lastname=lastname, age=age, email=email, password=hash_pw)
    return redirect('/')

def login_process(request):
    email = request.POST['email']
    password = request.POST['password']
    if not User.objects.authenticate(email, password):
        messages.error(request, 'email and password did not match our records')
        return redirect('/login')