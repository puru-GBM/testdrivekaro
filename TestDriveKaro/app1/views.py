from django.shortcuts import render
from .models import Contact

# Create your views here.

def index(request):
    return render(request,'index.html')
def ind(request):
    return render(request,'index.html')

def luxury(request):
    return render(request,'luxury.html')

def topbrand(request):
    return render(request,'topbrand.html')

def topchoice(request):
    return render(request,'topchoice.html')

def featuredcar(request):
    return render(request,'featuredcar.html')

def royal(request):
    return render(request,'royal.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phono', '')
        subject=request.POST.get('subject', '')
        message=request.POST.get('message', '')
        print(name,email,phone,subject,message)
        contact=Contact(name=name,email=email,contact=phone,Subject=subject,message=message)
        contact.save()
    return render(request,'contact.html')

def privacy(request):
    return render(request,'privacy.html')

def term(request):
    return render(request,'term.html')

def about(request):
    return render(request,'about.html')