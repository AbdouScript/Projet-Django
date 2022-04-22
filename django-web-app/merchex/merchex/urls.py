# ~/Projet-Django/django-web-app/merchex/merchex/urls.py

from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    # path('about-us/', views.about),  # ajoutez cette ligne
    # path('contact/', views.contact),  # ajoutez cette ligne
]