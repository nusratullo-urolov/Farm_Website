from django.urls import path

from apps.views import register, login_1, combine, tractor, mineral_endorsement, worker, other_equipment, home, elon, \
    contact, add_advert

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_1, name='login'),
    path('combines/', combine, name='combine'),
    path('tractor/', tractor, name='tractor'),
    path('mineral_endorsement/', mineral_endorsement, name='mineral_endorsement'),
    path('workers/', worker, name='workers'),
    path('equipments/', other_equipment, name='equipments'),
    path('client/', elon, name='elom'),
    path('contact/', contact, name='contact'),
    path('ad-combine/', add_advert, name='add_advert')
]
