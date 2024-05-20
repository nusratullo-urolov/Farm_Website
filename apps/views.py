from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, PageNotAnInteger
from django.shortcuts import render, redirect

from apps.forms import RegisterForm, LoginForm
from apps.models import User, Combine, Tractor, Workers, OtherEquipments, MineralEndorsements, AdCombine, AdTractor, \
    AdMineral, AdWorker, AdEquipment, AdFarm


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


def elon(request):
    return render(request, 'elon/index.html')


def contact(request):
    return render(request, 'contact.html')


def add_advert(request):
    if request.method == 'POST':
        data = request.POST
        def convert_to_int(value):
            return 1 if value.lower() in ('true', 'on', '1') else 0

        AdCombine.objects.create(c_name=data['c_name'],
                                 c_quantity=data['c_quantity'],
                                 c_price=data['c_price'],
                                 c_driver=convert_to_int(data.get('c_driver', '0')),
                                 c_quickly=convert_to_int(data.get('c_quickly', '0'))
                                 )
        AdTractor.objects.create(t_name=data['t_name'],
                                 t_quantity=data['t_quantity'],
                                 t_price=data['t_price'],
                                 t_driver=convert_to_int(data.get('t_driver', '0')),
                                 t_quickly=convert_to_int(data.get('t_quickly', '0'))
                                 )
        AdMineral.objects.create(m_name=data['m_name'],
                                 m_price=data['m_price'],
                                 m_weight=data['m_weight'],
                                 m_quickly=convert_to_int(data.get('m_quickly', '0'))
                                 )
        AdWorker.objects.create(w_name=data['w_name'],
                                w_quantity=data['w_quantity'],
                                w_price=data['w_price'],
                                w_quickly=convert_to_int(data.get('w_quickly', '0'))
                                )
        AdEquipment.objects.create(e_name=data['e_name'],
                                   e_quantity=data['e_quantity'],
                                   e_price=data['e_price'],
                                   e_quickly=convert_to_int(data.get('e_quickly', '0'))
                                   )

        AdFarm.objects.create(f_name=data['f_name'],
                              f_quantity=data['f_quantity'],
                              f_price=data['f_price'],
                              f_quickly=convert_to_int(data.get('f_quickly', '0'))
                              )
        return redirect('/')
