from django.urls import path

from django.conf.urls import include, url

from . import views

urlpatterns = [
    path('', views.templay),
    path('staff/', views.staff),
    path('form/', views.form),
]