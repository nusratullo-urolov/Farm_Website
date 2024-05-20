from django.urls import path

from apps.views import register, login_1, combine, tractor, mineral_endorsement, worker, other_equipment, home, \
    contact, add_advert, ad_combine, ad_tractor, ad_mineral, ad_equipment, ad_worker, ad_farm, information, soturidnik, \
    agrofond

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_1, name='login'),
    path('combines/', combine, name='combine'),
    path('tractor/', tractor, name='tractor'),
    path('mineral_endorsement/', mineral_endorsement, name='mineral_endorsement'),
    path('workers/', worker, name='workers'),
    path('equipments/', other_equipment, name='equipments'),
    path('ad-combine/', ad_combine, name='ad_combine'),
    path('ad-tractor/', ad_tractor, name='ad_tractor'),
    path('ad-mineral/', ad_mineral, name='ad_mineral'),
    path('ad-equipment/', ad_equipment, name='ad_equipment'),
    path('ad-worker/', ad_worker, name='ad_worker'),
    path('ad-farm/', ad_farm, name='ad_farm'),
    path('contact/', contact, name='contact'),
    path('add-advert/', add_advert, name='add_advert'),
    path('information/', information, name='information'),
    path('soturidnik/', soturidnik, name='soturidnik'),
    path('agro-fond/', agrofond, name='agrofond')
]
