from django.contrib import admin
from django.urls import path
from misc import views as misc_views

app_name = 'misc'

urlpatterns = [
    path('about-us/', misc_views.aboutus, name='about')
]
