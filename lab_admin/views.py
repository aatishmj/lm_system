from django.shortcuts import render 
from .models import ticket

# Create your views here.
def hello(request):
    return render(request , "admin_dash.html")

def problem(request):
    if request.method=="POST":
        id_list=[]
        tickets = ticket.objects.all()
        a=tickets.exists()
        if a : 

            last=ticket.objects.last()
            l_id=last.id
            for ids in range(1 , l_id+1) :
                if request.POST.get(str(ids)) != None :
                    id=request.POST.get(str(ids))  
                    id_list.append(id)
            for ids in id_list:
                instance = ticket.objects.get(id=ids)
                instance.delete()    
        return render(request, 'student_query.html', {'tickets': tickets})
    tickets = ticket.objects.all()
    return render(request, 'student_query.html', {'tickets': tickets})
    
    