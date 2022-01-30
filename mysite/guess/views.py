from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from howie.zero_shot_feelings import feeling_need_guesser

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

from django.http import JsonResponse

import logging

# Create your views here.
@login_required
def guess(request):
    #message = request.POST['message']
    #return HttpResponse("Hello, world!"+message)
    return render(request, 'guess/guess.html')

@login_required
def hello_world(request):
    return HttpResponse("Hello, world!")

@login_required
def feeling_need_guesser(request):
    #print(dir(request))
    print("method = ",request.method )
    print("body = ",request.body)
    #return HttpResponse("Guessing")
    return JsonResponse({"my_data":"yay data received"})

    