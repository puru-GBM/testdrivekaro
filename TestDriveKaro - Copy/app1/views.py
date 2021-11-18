from django.shortcuts import render

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
    return render(request,'contact.html')

def privacy(request):
    return render(request,'privacy.html')

def term(request):
    return render(request,'term.html')

def about(request):
    return render(request,'about.html')