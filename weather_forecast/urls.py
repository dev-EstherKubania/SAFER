from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('about/',views.about, name = 'about'),
    path('emergency_contacts/', views.emergency_contacts, name='emergency_contacts'),
]