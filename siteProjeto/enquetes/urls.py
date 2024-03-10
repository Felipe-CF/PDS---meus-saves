from django.urls import path
from . import views

urlpatterns= [
    path('dama/', views.index, name='index')
]