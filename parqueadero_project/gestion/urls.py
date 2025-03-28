# gestion/urls.py

from django.urls import path
from .views import custom_login, main_view, logout_view

urlpatterns = [
    path('login/', custom_login, name='login'),
    path('main/', main_view, name='main'),
    path('logout/', logout_view, name='logout'),
]
