from django.urls import path
from . import views

urlpatterns = [
    path('', views.stu_list, name='stu_list'),
]