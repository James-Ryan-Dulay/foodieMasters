from django.db import models
import bcrypt, re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def register_validate(self, post_data):
        errors = {}
        if not len(post_data['firstname']) or not len(post_data['lastname']) or not len(post_data['age']) or not len(post_data['email']) or not len(post_data['password']) or not len(post_data['confirm_password']):
            errors['all'] = 'Please fill out all forms'
            return errors
        if len(post_data['firstname']) < 2:
            errors['firstname'] = 'Firstname should be at least 3 characters'
        if len(post_data['lastname']) < 2:
            errors['lastname'] = 'Lastname should be at least 3 characters'
        if int(post_data['age']) < 6:
            errors['age'] = 'You should be at least 6 years old to register'
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = 'Please type a valid email address'
        if len(post_data['password']) < 7:
            errors['password'] = 'Password minimum requirement of 8 characters'
        if post_data['confirm_password'] != post_data['password']:
            errors['confirm_password'] = 'Confirm password did not match password'
        return errors

    def authenticate(self, email, password):
        users = self.filter(email=email)
        if not users:
            return False
        user = users[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())
        

class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField(default=5)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    objects = UserManager()

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

class PostManager(models.Manager):
    def post_validate(self, post_data):
        errors = {}
        if len(post_data['title']) < 2:
            errors['title'] = 'Title should at least be 3 characters'
        if len(post_data['description']) < 10:
            errors['description'] = 'Description minimum of 10 characters and maximum of 180 characters only'
        if len(post_data['recipe']) == 0:
            errors['recipe'] = 'Please put the recipe of the food'
        return errors

class Post(models.Model):
    title = models.CharField(max_length=180)
    description = models.CharField(max_length=255)
    recipe = models.TextField(default=0)
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    objects = PostManager()

    def __str__(self):
        return f'{self.user}'
