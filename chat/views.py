from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
# def room(request, room_name):
    
#     return render(request, 'chat/room.html', {'room_name_json': room_name})

def create_room(request):
    if request.method == 'POST':
        room_name = request.POST['room_name']
        return redirect(reverse('room', kwargs={'room_name': room_name}))
    return render(request, 'chat/create_room.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {'room_name_json': room_name})