from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_calc, name='main_calc')
]