from django.urls import path

from apps.views import register, login_1, combine, tractor, mineral_endorsement, workers, other_equipments, home

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_1, name='login'),
    path('combines/', combine, name='combine'),
    path('tractor/', tractor, name='tractor'),
    path('mineral_endorsement/', mineral_endorsement, name='mineral_endorsement'),
    path('workers/', workers, name='workers'),
    path('equipments/', other_equipments, name='equipments')
]
