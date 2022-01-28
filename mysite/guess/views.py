from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from howie.zero_shot_feelings import feeling_need_guesser

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

# Create your views here.
def guess(request):
    message = request.POST['message']
    return HttpResponse("Hello, world!"+message)

def hello_world(request):
    return HttpResponse("Hello, world!")


def feeling_need_guesser_inst(message):
    my_guesser = feeling_need_guesser()
    result_message = my_guesser.get_feelings(message)
    return result_message

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })