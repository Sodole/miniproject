from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request, "landing.html")

def signin(request):
    return render(request, "signin.html")

def signup(request):
    return render(request, "signup.html")

def index(request):
    return render(request, "index.html")

def detail(request):
    return render(request, "detail.html")

def input(request):
    return render(request, "input.html")

def record(request):
    return render(request, "record.html")

def realtime(request):
    return render(request, "realtime.html")