from django.shortcuts import render
from .models import *

def index(request):
  #blog = blog.objects.all
  return render(request , 'cogni/index.html')
