from django.db import models
from django.shortcuts import render

# Create your models here.
def index(request):
    return render(request, 'index.html')

def emergency_contacts(request):
    return render(request, 'emergency_contacts.html')

def about(request):
    return render(request, 'about.html')