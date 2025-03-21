from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='news_home'),
    path('create_news', views.create_news, name='add_news')
]
