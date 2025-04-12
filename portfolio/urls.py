# portfolio/urls.py (Create this file)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
]