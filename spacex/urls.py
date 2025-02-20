from django.urls import path
from . import views

urlpatterns = [
    path('', views.spacex_launches, name='spacex_launches'),
]
