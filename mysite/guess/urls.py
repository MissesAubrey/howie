# chat/urls.py
from django.urls import path


from . import views

urlpatterns = [
    path('guess', views.guess, name='guess'),
    path('hello', views.hello_world, name='hello_world'),
]