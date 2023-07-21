from django.shortcuts import render , HttpResponse , redirect
from lab_admin.models import signup_info
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout



def login(request):
    if request.method =="POST" :
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect("dboard")
        else:
            return render(request , "s_log.html") 


    return render(request , "s_log.html")

def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST['name']
        last_name = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        user=User.objects.create_user(first_name=first_name , last_name=last_name ,username=email , email=email , password=password )
        user.save()

        return render(request,"s_log.html")
    else:
        return render(request,'sign.html')

def dboard(request):
    if request.user.is_authenticated:
        return render(request , "dboard.html")

    else:
        return render(request , "s_log.html")

def logout_user(request):
    logout(request)
    return redirect("login")