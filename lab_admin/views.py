from django.shortcuts import render ,redirect
from .models import ticket , s_ticket,h_ticket
from django.contrib.auth import logout , login ,authenticate
# Create your views here.
# def hello(request):
#     return render(request , "admin_dash.html")

def hello(request):
    if request.method =="POST" :
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("adminpage")
        else:
            return render(request ,"login.html")

    return render(request ,"login.html")


def admin_dash(request) :
    if request.user.is_anonymous:
        print(request.user.is_anonymous)
        return redirect("hello")
    else:
        return render(request,"admin_dash.html")

def problem(request):
    if request.method=="POST":
        id_list=[]
        s_id_list=[]
        h_id_list=[]
        tickets = ticket.objects.all()
        sticket=s_ticket
        hticket=h_ticket
        a=tickets.exists()
        if a : 
            last=ticket.objects.last()
            l_id=last.id
            for ids in range(1 , l_id+1) :
                if request.POST.get(str(ids)) != None :
                    id=request.POST.get(str(ids))  
                    id_list.append(id)
                    print(type(id))
                if request.POST.get("s_issue") != None :
                    s_id=request.POST.get("s_issue")
                    if s_id not in s_id_list :
                        s_id_list.append(s_id)
                    print(s_id_list)
                if request.POST.get("h_issue") != None :
                    h_id=request.POST.get("h_issue")
                    if h_id not in h_id_list :
                        h_id_list.append(h_id)
                    print(h_id_list)
            for ids in s_id_list :
                instance = ticket.objects.get(id=ids)
                sticket=s_ticket(name=instance.name ,roll_no =instance.roll_no , pc_number=instance.pc_number , problem=instance.problem)
                sticket.save()
                if ids not in h_id_list :
                    instance.delete()

            for ids in h_id_list:
                instance = ticket.objects.get(id=ids)
                hticket=h_ticket(name=instance.name ,roll_no =instance.roll_no , pc_number=instance.pc_number , problem=instance.problem)
                hticket.save()
                instance.delete()                
            
            for ids in id_list:
                instance = ticket.objects.get(id=ids)
                instance.delete()    
        return render(request, 'student_query.html', {'tickets': tickets})
    tickets = ticket.objects.all()
    return render(request, 'student_query.html', {'tickets': tickets})
    

def s_page(request):
    if request.method=="POST":
        id_list=[]
        tickets = s_ticket.objects.all()
        a=tickets.exists()
        if a : 
            last=s_ticket.objects.last()
            l_id=last.id
            for ids in range(1 , l_id+1) :
                if request.POST.get(str(ids)) != None :
                    id=request.POST.get(str(ids))  
                    id_list.append(id)
            for ids in id_list:
                instance = s_ticket.objects.get(id=ids)
                instance.delete()    
        return render(request, 's_issue.html', {'tickets': tickets})       
    tickets = s_ticket.objects.all()
    return render(request, 's_issue.html', {'tickets': tickets})


def h_page(request):
    if request.method=="POST":
        id_list=[]
        tickets = h_ticket.objects.all()
        a=tickets.exists()
        if a : 
            last=h_ticket.objects.last()
            l_id=last.id
            for ids in range(1 , l_id+1) :
                if request.POST.get(str(ids)) != None :
                    id=request.POST.get(str(ids))  
                    id_list.append(id)
            for ids in id_list:
                instance = h_ticket.objects.get(id=ids)
                instance.delete()    
        return render(request, 'h_issue.html', {'tickets': tickets})       
    tickets = h_ticket.objects.all()
    return render(request, 'h_issue.html', {'tickets': tickets})