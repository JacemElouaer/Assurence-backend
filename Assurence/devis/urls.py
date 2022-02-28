"""Assurence URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    # les urls des devis appartment
    path('appartment/create', save_devis_apartment, name="save_devis_appartment"),
    path('appartment/get_all', get_devis_apartement, name="get_devis_appartment"),

    # les urls des devis maison
    path('maison/create', save_devis_maison, name="save_devis_maison"),
    path('maison/get_all', get_devis_maison, name="get_devis_maison"),

    # les urls des devis Immeuble
    path('immeuble/create', save_devis_immeuble, name="save_devis_maison"),
    path('immeuble/get_all', get_devis_immeuble, name="get_devis_maison")

]
