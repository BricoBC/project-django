from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hi(request, username):
    full = username + "_2509"
    return HttpResponse("<h1>Hello world %s</h1>" %full)

def about(request):
    return HttpResponse("About")