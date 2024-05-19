from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, PageNotAnInteger
from django.shortcuts import render, redirect

from apps.forms import RegisterForm, LoginForm
from apps.models import User, Combine, Tractor, Workers, OtherEquipments, MineralEndorsements


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


def combine(request):
    combines = Combine.objects.all()
    return render(request, 'kombayn.html', context={'combines': combines})


def tractor(request):
    tractors = Tractor.objects.all()
    return render(request, 'traktor.html', context={'tractor': tractors})


def mineral_endorsement(request):
    minerals = MineralEndorsements.objects.all()
    return render(request, 'ogit.html', context={'minerals': minerals})


def worker(request):
    workers = Workers.objects.all()
    return render(request, 'ishchi.html', context={'workers': workers})


def other_equipment(request):
    equipments = OtherEquipments.objects.all()

    return render(request, 'uskuna.html', context={'equipments': equipments})


def home(request):
    return render(request, 'asosiy.html')
