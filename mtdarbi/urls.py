"""mtdarbi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from darbi import views
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path
from darbi.views import ProjectList, CheckUpdatesView, DebtorList

urlpatterns = [
    path('', ProjectList.as_view(), name='index'),
    path('paradnieki/', DebtorList.as_view(), name='paradnieki'),
    path('api/check_updates/', CheckUpdatesView.as_view(), name='check_updates'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('admin/', admin.site.urls),
]