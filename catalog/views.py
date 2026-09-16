from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect

def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')

