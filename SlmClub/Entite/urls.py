"""Website URL Configuration

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
from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="index.html"),
    path("Parametre.html/", views.Parametre, name="Parametre.html"),
    path("Contact.html/", views.Contact, name="Contact.html"),
    path("Quittance.html/", views.quittance_view, name="Quittance.html"),
    path("Commune.html/", views.commune_view, name="Commune.html"),
    path("Menbre.html/", views.Menbre_view, name="Menbre.html"),
    path("Categorie.html/", views.Categorie_view, name="Categorie.html"),
    path("create_Quittance.html/", views.create_quittance, name="create_Quittance.html"),
    path("create_Commune.html/", views.create_commune, name="create_Commune.html"),
    path("create_Categorie.html/", views.create_categorie, name="create_Categorie.html"),
    path("create_Menbre.html/", views.create_menbre, name="create_Menbre.html"),
    path('modify_quittance.html/<int:quittance_id>/', views.modify_quittance, name='modify_quittance'),
    path('communes/modify/<int:commune_id>/', views.modify_commune, name='modify_commune'),
    path('modify_categorie/<int:categorie_id>/', views.modify_categorie, name='modify_categorie'),
    path('modify_menbre/<int:menbre_id>/', views.modify_menbre, name='modify_menbre'),
    path('delete_quittance/<int:quittance_id>/', views.delete_quittance, name='delete_quittance'),
    path('communes/delete/<int:commune_id>/', views.delete_commune, name='delete_commune'),
    path('delete_categorie/<int:categorie_id>/', views.delete_categorie, name='delete_categorie'),
    path('delete_menbre/<int:menbre_id>/', views.delete_menbre, name='delete_menbre'),
    
    

    
]
