"""merchex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/',views.band_list, name='band-list'),
    path('about-us/',views.about,name="about"),
    path('listings/',views.annonce_list, name='annonce-list'),
    path('contact/',views.contact,name='contact'),

    #url pour le lien cliqué
    path('bands/<int:id>/',views.band_detail,name='band-detail'),
    path('listings/<int:id>/',views.annonce_detail, name='annonce-detail'),
    path('listings/add/',views.annonce_create, name='annonce-create'),

    path('bands/add/',views.band_create,name='band-create'),

    #url de page de redirection
    path('email-sent/',views.confirmation,name="redirect"),

    #Mise à jour d'un Band et d'une annonce
    path('bands/<int:id>/change/',views.update_band,name="band-update"),
    path('listings/<int:id>/change/',views.update_annonce, name='annonce-update'),

    #suppression de la Base de données
    path('bands/<int:id>/delete/',views.delete_band,name='band-delete'),
    path('listings/<int:id>/delete/',views.delete_annonce,name='annonce-delete'),

]   
