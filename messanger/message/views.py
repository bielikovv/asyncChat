from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import logout, login



def get_main_page(request):
    return render(request, 'message/main_page.html')



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat')
    else:
        form = RegistrationForm()
    return render(request, 'message/register.html', {'form': form})



def login_func(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('chat')
    else:
        form = LoginForm()
    return render(request, 'message/login.html', {'form': form})



def logout_func(request):
    logout(request)
    return redirect('chat')



def index(request):
    return render(request, 'message/index.html')



def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    messages = Message.objects.filter(room=room_name)[0:25]
    return render(request, 'message/room.html', {'room_name': room_name, 'username':username, 'messages': messages})



def get_user(request):
    user = request.user
    return render(request, 'message/index.html', {'user':user})

