from re import A
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
    user = User.objects.get(email=email)
    request.session['user_firstname'] = user.firstname
    request.session['user_id'] = user.id
    return redirect('/main')

def main(request):
    if 'user_id' not in request.session:
        return HttpResponse('<h1> Please log in to access FoodieMasters main page. </br> Back to login page <a href="/login">Login</a> or register instead <a href="/">register</a> </h1>')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'main.html', context)

def logoff(request):
    del request.session['user_id']
    request.session.clear()
    return redirect('/')

def post(request):
    if 'user_id' not in request.session:
        return HttpResponse('<h1> Please log in to access FoodieMasters. </br> Back to login page <a href="/login">Login</a> or register instead <a href="/">register</a> </h1>')
    return render(request, 'post.html')

def post_process(request):
    if 'user_id' not in request.session:
        return HttpResponse('<h1> Please log in to access FoodieMasters. </br> Back to login page <a href="/login">Login</a> or register instead <a href="/">register</a> </h1>')
    errors = Post.objects.post_validate(request.POST)
    title = request.POST['title']
    description = request.POST['description']
    recipe = request.POST['recipe']
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/post')
    user = User.objects.get(id=request.session['user_id'])
    Post.objects.create(title=title, description=description, recipe=recipe, user=user)
    return redirect('/main')

def profile(request):
    if 'user_id' not in request.session:
        return HttpResponse('<h1> Please log in to access FoodieMasters. </br> Back to login page <a href="/login">Login</a> or register instead <a href="/">register</a> </h1>')
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'profile.html', context)

def delete_post(request, post_id):
    to_delete = Post.objects.get(id=post_id)
    to_delete.delete()
    return redirect('/profile')

def edit_post(request, edit_id):
    post = Post.objects.get(id=edit_id)
    context = {
        'post' : post
    }
    return render(request, 'edit_post.html', context)

def modify_post(request):
    post_id = request.POST['post_id']
    errors = Post.objects.post_validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/edit_post/{post_id}')
    modify_post = Post.objects.get(id=post_id)
    title = request.POST['title']
    description = request.POST['description']
    recipe = request.POST['recipe']
    modify_post.title = title
    modify_post.description = description
    modify_post.recipe = recipe
    modify_post.save()
    return redirect('/profile')