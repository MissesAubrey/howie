from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from howie.zero_shot_feelings import feeling_need_guesser

# Create your views here.
@login_required
def index(request):
    return render(request, 'chat/index.html', {})

@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

def feeling_need_guesser_inst(message):
    my_guesser = feeling_need_guesser()
    result_message = my_guesser.get_feelings(message)
    return result_message
