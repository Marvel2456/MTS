from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('customer/', views.CustomerList.as_view()),
    path('customer/<int:pk>/', views.CustomerDetail.as_view()),
    path('male/', views.MaleList.as_view()),
    path('male/<int:pk>/', views.MaleDetail.as_view()),
    path('female/', views.FemaleList.as_view()),
    path('female/<int:pk>/', views.FemaleDetail.as_view()),
    path('staff/', views.StaffList.as_view()),
    path('staff/<int:pk>/', views.StaffDetail.as_view()),
    path('tailor/', views.TailorList.as_view()),
    path('tailor/<int:pk>/', views.TailorDetail.as_view()),
    path('clothe/', views.ClotheList.as_view()),
    path('clothe/<int:pk>/', views.ClotheDetail.as_view()),
    path('appointment/', views.AppointmentList.as_view()),
    path('appointment/<int:pk>/', views.AppointmentDetail.as_view()),
    path('style/', views.StyleList.as_view()),
    path('style/<int:pk>/', views.StyleDetail.as_view()),
    path('regin/', views.RegisterInList.as_view()),
    path('regin/<int:pk>/', views.RegisterInDetail.as_view()),
    path('regout/', views.RegisterOutList.as_view()),
    path('regout/<int:pk>/', views.RegisterOutDetail.as_view()),
    path('entry/', views.EntryList.as_view()),
    path('entry/<int:pk>/', views.EntryDetail.as_view()),
]
