# chat/urls.py
from django.urls import path


from . import views

urlpatterns = [
    path('', views.guess, name='guess'),
    path('guess', views.my_guesser, name='my_guess'),
    path('hello', views.hello_world, name='hello_world'),
    path('static/guess/', views.my_guess_style, name='my_guess_style'),
]