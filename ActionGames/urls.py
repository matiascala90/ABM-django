"""
URL configuration for ActionGames project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Tienda import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('registrarse/',views.registrarse,name='registrarse'),
    path('juegos/',views.juegos,name='juegos'),
    path('juegos/create',views.Crear_juego,name='crear_juegos'),
    path('companias/',views.compania,name='company'),
    path('companias/create/',views.crear_compania,name='crear_compania'),
    path('plataformas/',views.plataforma,name='plataform'),
    path('plataformas/create/',views.crear_plataforma,name='crear_plataforma'),
    path('generos/',views.genero,name='gender'),
    path('generos/create/',views.crear_genero,name='crear_genero'),
    path('login/',views.logIn,name='login'),
    path('logout/',views.logOut,name='logout'),
    path('juegos/<int:juego_id>/',views.juegos_detalle,name='juego_detalle'),
    path('juegos/<int:juego_id>/delete/',views.delete_juego,name='delete_juego'),
    path('companias/<int:compania_id>/',views.compania_detalle,name='compania_detalle'),
    path('companias/<int:compania_id>/delete/',views.delete_compania,name='delete_compania'),
    path('plataformas/<int:plataforma_id>/',views.plataforma_detalle,name='plataforma_detalle'),
    path('plataformas/<int:plataforma_id>/delete/',views.delete_plataforma,name='delete_plataforma'),
    path('generos/<int:genero_id>/',views.genero_detalle,name='genero_detalle'),
    path('generos/<int:genero_id>/delete/',views.delete_genero,name='delete_genero'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

