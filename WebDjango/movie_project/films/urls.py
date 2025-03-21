from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='films'),
    path('create', views.create_form, name='create'),
]