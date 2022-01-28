# chat/urls.py
from django.urls import path


from . import views

urlpatterns = [
    path('', views.guess, name='guess'),
    path('hello', views.hello_world, name='guess'),
    path('password/', views.change_password, name='change_password'),
]