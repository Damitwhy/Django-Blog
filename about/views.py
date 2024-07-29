from django.shortcuts import render
from django.views import generic

# Create your views here.

class about(request):
    return render(request, 'about/about.html')