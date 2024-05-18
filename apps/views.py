from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, PageNotAnInteger
from django.shortcuts import render, redirect

from apps.forms import RegisterForm, LoginForm
from apps.models import User


# Create your views here.


def register(request):
    if request.method == 'POST':
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
        else:
            print(forms.errors)
        return redirect('login')
    return render(request, 'auth/auth.html')


def login_1(request):
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.data.get('email')
            password = forms.data.get('password')
            users = authenticate(username=username, password=password)
            if users:
                login(request, users)
                return redirect('home')
    return render(request, 'auth/auth.html')