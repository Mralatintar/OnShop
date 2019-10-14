from django.shortcuts import render
from django.http import response
from django.shortcuts import render
def index(request):
    return render(request,'buyer/index.html',locals())
# Create your views here.
