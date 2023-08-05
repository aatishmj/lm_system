from django.shortcuts import render 
from .models import ticket

# Create your views here.
def hello(request):
    return render(request , "admin_dash.html")

def problem(request):
    if request.method=="POST":
        id_list=[]
        tickets = ticket.objects.all()
        last=ticket.objects.last()
        # for ids in range(0,int(last.id)):
        #     id=request.POST.get(str(ids))    
        #     print(id)
        #     if id!="" and id!=None :
        #         id_list.append(id)
        id=request.POST.get("id")  
        print(id)
        tickets = ticket.objects.all()
        for ids in id :
            instance = ticket.objects.get(id=ids)
            instance.delete()
        print(id)
        return render(request, 'student_query.html', {'tickets': tickets})
    tickets = ticket.objects.all()
    return render(request, 'student_query.html', {'tickets': tickets})
    
    