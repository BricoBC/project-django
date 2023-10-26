from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hi(request, username):
    print(type(username))
    return HttpResponse("<h1>Hello world %s</h1>" %username)

def about(request):
    return HttpResponse("About")