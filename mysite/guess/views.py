import os
import json
import requests

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from howie.zero_shot_feelings import feeling_need_guesser

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.conf import settings

from django.http import JsonResponse

from howie.zero_shot_feelings import feeling_need_guesser

too_many_guessers = feeling_need_guesser()

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
def my_guess_style(request):
    css_path = os.path.join(settings.BASE_DIR,'mysite/static/guess/style.css')
    my_file = open(css_path, 'r')
    #response = HttpResponse(content=requests.get("http://localhost:3000/static/guess/style.css").text)
    response = HttpResponse(content=my_file.read())
    response['Content-Type'] = 'text/css'

    return response

@login_required
def my_guesser(request):

    body = json.loads(request.body.decode("utf-8"))
    if (False):
        print('request.body = ', request.body)
        print("method = ",request.method )
        print("request.body.decode('utf-8') = ", request.body.decode("utf-8"))
        print("type(request.body.decode('utf-8')) = ", type(request.body.decode("utf-8")))
        print("json.loads(request.body.decode('utf-8')) = ", json.loads(request.body.decode("utf-8")))
        print("decoded_message['story'] = ",body['story'])

    print("method = ",request.method, "user = ", request.user)
    
    if  len(body['story']) > 500:
        result_message = "Not enough GPU memory. Please keep message below 500 characters"
    else:
        too_many_guessers.num_needs = int(body['num_needs'])
        too_many_guessers.num_feelings = int(body['num_feelings'])
        result_message = too_many_guessers.get_feelings(body['story'])

    return JsonResponse({"my_data":result_message})

    