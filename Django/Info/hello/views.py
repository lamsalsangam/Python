from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("Hello, World")
    return render(request, 'hello/index.html')

def geek(request):
    return HttpResponse("You there Doing good")

def greet(request, name):
    return render(request, 'hello/greet.html', {
        'name': name.capitalize(),
    })