from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'age', 'email', 'password', 'confirm_password')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'recipe', 'user')

@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = ('file', 'user')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text','user','post')
