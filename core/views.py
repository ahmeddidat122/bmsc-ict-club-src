from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, 'core/home.html', {'year' : datetime.now().year})

def About(request):
    return render(request, 'core/about.html', {'year' : datetime.now().year})

def events(request):
    return render(request, 'core/events.html', {'year' : datetime.now().year})

def blogs(request):
    return render(request, 'core/blogs.html', {'year' : datetime.now().year})

def contact(request):
    return render(request, 'core/contact.html', {'year' : datetime.now().year})