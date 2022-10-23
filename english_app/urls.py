from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get', views.get_data, name='getting'),
    path('add', views.put_data, name='add')
]
