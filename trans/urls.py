from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('create/', views.trans_create, name='trans_create'),
]