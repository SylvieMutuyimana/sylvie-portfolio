from django.contrib import admin
from django.urls import path, include
from .views import check, contact, home,profile_card, about
urlpatterns = [
    path('check', check, name='check'),

    path('contact', contact, name='contact'),
    path('', home, name='home'),
 
    path('profilecard', profile_card, name='profile_card'),
    path('about', about, name='about'),



]
