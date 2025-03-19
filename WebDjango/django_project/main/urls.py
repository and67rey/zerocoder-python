from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('team', views.team, name='team'),
    path('contacts', views.contacts, name='contacts')
]
