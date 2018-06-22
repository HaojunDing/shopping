from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def add(request):
    return render(request,'myadmin/add.html')