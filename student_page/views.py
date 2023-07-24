from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout , login
from django.contrib import messages



def login_user(request):
    if request.method =="POST" :
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dboard")
        else:
            return render(request ,"s_log.html") 


    return render(request ,"s_log.html")

def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST.get('name')
        last_name = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user=User.objects.create_user(first_name=first_name , last_name=last_name ,username=email , email=email , password=password )
        user.save()
        return  redirect("login")
    else:
        return render(request,'sign.html')

def dboard(request):
    if request.user.is_anonymous:
        print(request.user.is_anonymous)
        return redirect("login")
    else:
        if request.method == 'POST':
            messages.success(request, 'Your response has succesfully recorded.')
        return render(request,"dboard.html")
    

def logout_user(request):
    logout(request)
    return redirect("login")