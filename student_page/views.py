from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request , "s_log.html")

def signup(request):
    return render(request , "signup.html")

def dboard(request):
    return render(request , "dboard.html")
