from django.shortcuts import render, redirect
from .models import UserProgress, UserProfile, Login, Logout, PasswordChange, UserCreation
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import RedirectView

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=form.cleaned_data['username'])
            UserCreation.objects.create(user=user)
            return redirect('login')

def user_profile(request, username):
    user = User.objects.get(username=username)
    profile = UserProfile.objects.get(user=user)
    return render(request, 'authentication/user_profile.html', {'profile': profile})  

def login(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.POST['username'])
        Login.objects.create(user=user)
        return redirect('index')
    
def logout(request):
    logout(request)
    return redirect('login')

def password_change(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.POST['username'])
        PasswordChange.objects.create(user=user)
        return redirect('index')

