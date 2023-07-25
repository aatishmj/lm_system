from django.shortcuts import render 
from .models import ticket

# Create your views here.
def hello(request):
    return render(request , "admin_dash.html")

def problem(request):
    if request.method=="POST" :
        tickets = ticket.objects.all()
    return render(request, 'student_query.html', {'tickets': tickets})
    