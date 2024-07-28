"""
URL configuration for plus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app1 import views  # Import views from your application


urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('show-employees/', views.show_employees, name='show-employees'),
    path('add-employees/', views.add_employees, name='add-employees'),
    path('edit-employees/<int:eid>/', views.edit_employees, name='edit-employees'),
    path('delete-employees/<int:eid>/', views.delete_employees, name='delete-employees'),
    
]
