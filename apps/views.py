from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger
from django.shortcuts import render, redirect
from django.urls import reverse

from apps.forms import RegisterForm, LoginForm
from apps.models import User, Combine, Tractor, Workers, OtherEquipments, MineralEndorsements, AdCombine, AdTractor, \
    AdMineral, AdWorker, AdEquipment, AdFarm
from django.contrib import messages

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
            username = forms.data.get('username')
            password = forms.data.get('password')
            users = authenticate(username=username, password=password)
            if users:
                login(request, users)
                return redirect('home')
            else:
                messages.add_message(request,
                                     level=messages.ERROR,
                                     message='email or password wrong'
                                     )
                return render(request, 'auth/auth.html')
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


@login_required(login_url='/login')
def home(request):
    return render(request, 'asosiy.html')


def contact(request):
    return render(request, 'contact.html')


def add_advert(request):
    if request.method == 'POST':
        data = request.POST

        def convert_to_int(value):
            return 1 if value.lower() in ('true', 'on', '1') else 0

        try:
            AdCombine.objects.create(
                c_name=data['c_name'],
                c_quantity=data['c_quantity'],
                c_price=data['c_price'],
                c_driver=convert_to_int(data.get('c_driver', '0')),
                c_quickly=convert_to_int(data.get('c_quickly', '0')),
                from_date=data['c_fromdate'],
                to_date=data['c_todate'],
            )
        except (KeyError, ValueError) as e:
            print(f"Error creating AdCombine: {e}")

        try:
            AdTractor.objects.create(
                t_name=data['t_name'],
                t_quantity=data['t_quantity'],
                t_price=data['t_price'],
                t_driver=convert_to_int(data.get('t_driver', '0')),
                t_quickly=convert_to_int(data.get('t_quickly', '0')),
                from_date=data['t_fromdate'],
                to_date=data['t_todate'],
            )
        except (KeyError, ValueError) as e:
            print(f"Error creating AdTractor: {e}")

        try:
            AdMineral.objects.create(
                m_name=data['m_name'],
                m_price=data['m_price'],
                m_weight=data['m_weight'],
                m_quickly=convert_to_int(data.get('m_quickly', '0')),
                from_date=data['m_fromdate'],
                to_date=data['m_todate'],
            )
        except (KeyError, ValueError) as e:
            print(f"Error creating AdMineral: {e}")

        try:
            AdWorker.objects.create(
                w_name=data['w_name'],
                w_quantity=data['w_quantity'],
                w_price=data['w_price'],
                w_quickly=convert_to_int(data.get('w_quickly', '0')),
                from_date=data['w_fromdate'],
                to_date=data['w_todate'],
            )
        except (KeyError, ValueError) as e:
            print(f"Error creating AdWorker: {e}")

        try:
            AdEquipment.objects.create(
                e_name=data['e_name'],
                e_quantity=data['e_quantity'],
                e_price=data['e_price'],
                e_quickly=convert_to_int(data.get('e_quickly', '0')),
                from_date=data['e_fromdate'],
                to_date=data['e_todate'],
            )
        except (KeyError, ValueError) as e:
            print(f"Error creating AdEquipment: {e}")

        try:
            AdFarm.objects.create(
                f_name=data['f_name'],
                f_quantity=data['f_quantity'],
                f_price=data['f_price'],
                f_quickly=convert_to_int(data.get('f_quickly', '0')),
                from_date=data['f_fromdate'],
                to_date=data['f_todate']
            )
        except (KeyError, ValueError) as e:
            print(f"Error creating AdFarm: {e}")

        return redirect('information')


def ad_combine(request):
    combines = AdCombine.objects.order_by('-id')
    return render(request, 'elon/combine.html', context={'combines': combines})

def ad_tractor(request):
    tractors = AdTractor.objects.order_by('-id')
    return render(request, 'elon/tractor.html', context={'tractors': tractors})

def ad_mineral(request):
    minerals = AdMineral.objects.order_by('-id')
    return render(request, 'elon/mineral.html', context={'minerals': minerals})

def ad_worker(request):
    workers = AdWorker.objects.order_by('-id')
    return render(request, 'elon/worker.html', context={'workers': workers})

def ad_equipment(request):
    equipments = AdEquipment.objects.order_by('-id')
    return render(request, 'elon/equipment.html', context={'equipments': equipments})

def ad_farm(request):
    farms = AdFarm.objects.order_by('-id')
    return render(request, 'elon/farm.html', context={'farms': farms})

def information(request):
    return render(request, 'elon/information.html')

def soturidnik(request):
    return render(request, 'sotrudnik.html')

def agrofond(request):
    return render(request, 'agrofond.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def yer(request):
    return render(request, 'yer.html')