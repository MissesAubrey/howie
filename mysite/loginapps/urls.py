# chat/urls.py
from django.urls import path


from . import views

urlpatterns = [
    path('password/', views.change_password, name='change_password'),
]