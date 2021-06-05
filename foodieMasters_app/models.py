from django.db import models
import bcrypt, re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def register_validate(self, post_data):
        errors = {}
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

class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField(default=5)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)

    objects = UserManager()

