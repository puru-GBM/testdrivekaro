from django.db import models
from django.shortcuts import render
from math import ceil
from .models import Contact, filter_luxury, filter_top

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

def filterdata(request):
    cars = filter_top.objects.all()
    cars2 = filter_luxury.objects.all()
    brand=[]
    # # print(cars)
    n=len(cars)
    # # print(n)
    nslides= n//4 + ceil((n/4 - (n//4)))
    if request.method=="POST":
        topbrand=request.POST.get('topbrand',"no") 
        luxury=request.POST.get('luxury',"no")
        color=request.POST.get('color',"no")
        price=request.POST.get('price',"no")
        # print(topbrand,luxury)
        if topbrand == "":
            print(topbrand)
            prices = price.split()    
            prices[0]=int(prices[0])
            prices[2]=int(prices[2])
            # print(prices[0])
            # print(prices[2])
            for i in range(n):
        
                if cars[i].TopBrands == topbrand and cars[i].color == color and prices[0] <= cars[i].Price <= prices[2]:
                    data={
                        'topbrand' : cars[i].TopBrands,
                        'model'    : cars[i].model,
                        'color': cars[i].color,
                        'price':cars[i].Price,
                        'img' :cars[i].img,
                        'url':cars[i].url,
                        }
                    brand.append(data)
                    # print(brand)
            params={'no_of_slides':nslides, 'range':range(nslides) ,'car':brand}
            return render(request,'filterdata.html',params)
        
        elif topbrand == "maruti" :
            print(topbrand,color, price)
            # print(prices[0])
            # print(prices[2])
            if topbrand =="maruti" and color=='no' and price=='no':

                for i in range(n):
        
                    if cars[i].TopBrands == topbrand:
                        data={
                            'topbrand' : cars[i].TopBrands,
                            'model'    : cars[i].model,
                            'color': cars[i].color,
                            'price':cars[i].Price,
                            'img' :cars[i].img,
                            'url':cars[i].url,
                        }
                        brand.append(data)
                        # print(brand)
               
            if topbrand =="maruti" and color!='no' and price=='no':
                # prices = price.split()    
                # prices[0]=int(prices[0])
                # prices[2]=int(prices[2])
                for i in range(n):
                    if cars[i].TopBrands == topbrand and cars[i].color == color  :
                        data={
                            'topbrand' : cars[i].TopBrands,
                            'model'    : cars[i].model,
                            'color': cars[i].color,
                            'price':cars[i].Price,
                            'img' :cars[i].img,
                            'url':cars[i].url,
                            }
                        brand.append(data)
                        # print(brand)
           
            if topbrand =="maruti" and color!='no' and price!='no':
                prices = price.split()    
                prices[0]=int(prices[0])
                prices[2]=int(prices[2])
                for i in range(n):
                    if cars[i].TopBrands == topbrand and cars[i].color == color  and prices[0] <= cars[i].Price <= prices[2]  :
                        data={
                            'topbrand' : cars[i].TopBrands,
                            'model'    : cars[i].model,
                            'color': cars[i].color,
                            'price':cars[i].Price,
                            'img' :cars[i].img,
                            'url':cars[i].url,
                            }
                        brand.append(data)
                        # print(brand)
            if topbrand =="maruti" and color=='no' and price!='no':
                prices = price.split()    
                prices[0]=int(prices[0])
                prices[2]=int(prices[2])
                for i in range(n):
                    if cars[i].TopBrands == topbrand and prices[0] <= cars[i].Price <= prices[2]  :
                        data={
                            'topbrand' : cars[i].TopBrands,
                            'model'    : cars[i].model,
                            'color': cars[i].color,
                            'price':cars[i].Price,
                            'img' :cars[i].img,
                            'url':cars[i].url,
                            }
                        brand.append(data)
                        # print(brand)
            params={'no_of_slides':nslides, 'range':range(nslides) ,'maruti':brand}
            return render(request,'filterdata.html',params)
        elif luxury=='no' and topbrand =="no" and color=='no' and price!='no':
            print(topbrand,color, price)
            prices = price.split()    
            prices[0]=int(prices[0])
            prices[2]=int(prices[2])
            for i in range(n):
                if  prices[0] <= cars[i].Price <= prices[2]  :
                    data={
                        'topbrand' : cars[i].TopBrands,
                        'model'    : cars[i].model,
                        'color': cars[i].color,
                        'price':cars[i].Price,
                        'img' :cars[i].img,
                        'url':cars[i].url,
                        }
                    brand.append(data)
                    print(brand)
            params={'no_of_slides':nslides, 'range':range(nslides) ,'car':brand}
            return render(request,'filterdata.html',params)

        else:
            params={'no_of_slides':nslides, 'range':range(nslides) ,'cars':cars}
            return render(request,'filterdata.html',params)
    