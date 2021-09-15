from django.urls import path

from .views import *

urlpatterns = [
    path('create-profile/', UserAPI.as_view() ,name='UserCreate'),
    path('profile/', UserListAPI.as_view() ,name='UserFullList'),
    path('profile/<int:user_id>/', UserAPI.as_view() ,name='UserProfile'),
    path('update-profile/<int:user_id>/', UserAPI.as_view() ,name='UserUpdate'),
    path('delete-profile/<int:user_id>/', UserAPI.as_view() ,name='UserDelete'),
    path('admin-login/', AdminAPI.as_view(), name='admin-login')
]
