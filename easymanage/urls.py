from django.conf.urls import url
from . import views
from django.urls import path,re_path
from . import views as easymanage_views
from django.contrib.auth import views as auth_views


app_name = 'easymanage'

urlpatterns = [

    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('', views.about, name='about'),
    url('about/', views.about, name='about'),
    url('customer_list/', views.customer_list, name='customer_list'),
    path('customer/new/', views.customer_new, name='customer_new'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    url('customerservice_list/', views.customerservice_list, name='customerservice_list'),
    path('customerservice/new/', views.customerservice_new, name='customerservice_new'),
    path('customerservice/<int:pk>/edit/', views.customerservice_edit, name='customerservice_edit'),
    path('customerservice/<int:pk>/delete/', views.customerservice_delete, name='customerservice_delete'),
    url('roomstatus_list/', views.roomstatus_list, name='roomstatus_list'),
    path('roomstatus/new/', views.roomstatus_new, name='roomstatus_new'),
    path('roomstatus/<int:pk>/edit/', views.roomstatus_edit, name='roomstatus_edit'),
    path('roomstatus/<int:pk>/delete/', views.roomstatus_delete, name='roomstatus_delete'),
    path('customer/<int:pk>/summary/', views.summary, name='summary'),
]
