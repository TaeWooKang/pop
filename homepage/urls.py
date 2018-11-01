"""POPtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import homepage.views as views
urlpatterns = [
    path('', views.main, name='main'),
    path('join/', views.join, name="join"),
    path('ID_check', views.ID_check, name="ID_check"),
    path('nick_check', views.nick_check, name="nick_check"),
    path('join_agree', views.join_agree, name="join_agree"),
    path('login/', views.login, name="login"),
]
