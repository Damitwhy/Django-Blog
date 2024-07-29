from django.shortcuts import render
from django.views import generic

# Create your views here.

def about(request):
    return render(request, 'about/about.html')