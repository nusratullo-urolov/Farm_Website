from django.urls import path

from apps.views import register, login_1

urlpatterns = [
    # path('',home,name='home'),
    path('register/',register,name='register'),
    path('login/',login_1,name='login')
]