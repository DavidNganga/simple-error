from django.shortcuts import render
from .models import Comment,error

# Create your views here.
def error(request):




    
    return(request, 'error.html')
