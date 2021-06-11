from django.urls import path
from . import views

urlpatterns = [
    path('', views.register),
    path('login', views.login),
    path('register_process', views.register_process),
    path('login_process', views.login_process),
    path('main', views.main),
    path('logoff', views.logoff),
    path('post/', views.post),
    path('post_process', views.post_process),
    path('profile', views.profile),
    path('delete_post/<int:post_id>', views.delete_post),
    path('edit_post/<int:edit_id>', views.edit_post),
    path('modify_post', views.modify_post),
    path('comment_process', views.comment_process),
    path('profile_comment_process', views.profile_comment_process),
    path('edit_profile', views.edit_profile ),
    path('edit_profile_process/<int:user_id>', views.edit_profile_process),
    path('like/<int:post_id>', views.like_post),
    path('add_profile/<int:user_id>', views.add_profile)
]
