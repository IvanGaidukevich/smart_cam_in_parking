"""
URL configuration for smart_cam_in_parking project.

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
from django.urls import path, include
from scip import views
from camera import views as cam


urlpatterns = [
    path('', views.show_arrives),
    path('vehicle/', views.show_all_vehicles),
    path('vehicle/create/', views.create_vehicle),
    path('vehicle/edit/<int:id>/', views.edit_vehicle),
    path('vehicle/delete/<int:id>/', views.delete_vehicle),
    path('owner/', views.show_all_owners),
    path('owner/create/', views.create_owner),
    path('owner/edit/<int:id>/', views.edit_owner),
    path('owner/delete/<int:id>/', views.delete_owner),
    path('admin/', admin.site.urls),
    path('camera/', cam.start),
    path('departures/', views.show_departures),
    path('arrives/', views.show_arrives),

]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
