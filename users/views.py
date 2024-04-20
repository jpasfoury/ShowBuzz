from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from django.shortcuts import render

# users/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'users/home.html')  # Render home.html template

def user_login(request):
    return render(request, 'users/login.html')  # Render login.html template

def user_register(request):
    return render(request, 'users/register.html')  # Render register.html template


def home(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'home.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')
