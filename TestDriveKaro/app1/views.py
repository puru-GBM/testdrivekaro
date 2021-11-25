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
    brands=[]
    # # print(cars)
    n=len(cars)
    n2=len(cars2)
    nn=n+n2
    nslides2= n2//4 + ceil((n2/4 - (n2//4)))
    # # print(n)
    filtered="Filtered Cars"
    
    nslides= n//4 + ceil((n/4 - (n//4)))
    if request.method=="POST":
        topbrand=request.POST.get('topbrand',"no") 
        luxury=request.POST.get('luxury',"no")
        color=request.POST.get('color',"no")
        price=request.POST.get('price',"no")
        lux="Luxury Cars"
        total="Total Car"
        top="Top Brands"
        if topbrand =='no' and luxury == 'no' and color =='no' and price=='no':
            # print(topbrand,luxury,color,price)

            params={'lux':lux,'top':top,'total':total,'length':nn,'lens':n,'len':n2, 'range':range(nslides) ,'range':range(nslides2) ,'car':cars,'ca':cars2}
            return render(request,'filterdata.html',params)
        
        
        
        else :
                    # XX--if top brand and there artibutes are on --XX
            if topbrand !='no' and luxury == 'no' and color =='no' and price=='no':            
                for i in range(n):
                    if topbrand==cars[i].TopBrands:
                        data={
                            'topbrand' : cars[i].TopBrands,
                            'model'    : cars[i].model,
                            'color': cars[i].color,
                            'price':cars[i].Price,
                            'img' :cars[i].img,
                            'url':cars[i].url,
                            }
                        brand.append(data)
                n1=len(brand)         
                params={'lux':lux,'total':filtered,'length':n1,'top':top,'lens':top, 'range':range(nslides)  ,'filt':brand,}
                return render(request,'filterdata.html',params)

            # XX-- brand and Color is on --xx
            elif topbrand !='no' and luxury == 'no' and color !='no' and price=='no':
                
                
                for i in range(n):
        
                    if topbrand==cars[i].TopBrands and color == cars[i].color:
                        data={
                            'topbrand' : cars[i].TopBrands,
                            'model'    : cars[i].model,
                            'color': cars[i].color,
                            'price':cars[i].Price,
                            'img' :cars[i].img,
                            'url':cars[i].url,
                            }
                        brand.append(data)
                  
                n1=len(brand)
            
                params={'lux':lux,'total':filtered,'length':n1,'top':top,'lens':top, 'range':range(nslides)  ,'filt':brand,}
                return render(request,'filterdata.html',params)

                # xx-- brand and price is on
            elif topbrand !='no' and luxury == 'no' and color =='no' and price !='no':                
                
                for i in range(n):
                    prices =price.split()
                    a=int(prices[0])
                    b=int(prices[2])
        
                    if topbrand==cars[i].TopBrands and cars[i].Price >= a and cars[i].Price <=b :
                        data={
                            'topbrand' : cars[i].TopBrands,
                            'model'    : cars[i].model,
                            'color': cars[i].color,
                            'price':cars[i].Price,
                            'img' :cars[i].img,
                            'url':cars[i].url,
                            }
                        brand.append(data) 
                n1=len(brand)

            
                params={'lux':lux,'total':filtered,'length':n1,'top':top,'lens':top, 'range':range(nslides)  ,'filt':brand,}
                return render(request,'filterdata.html',params)

                # xx---- brand color price is on here---- xx

            elif topbrand !='no' and luxury == 'no' and color !='no' and price!='no':  
                prices =price.split()
                a=int(prices[0])
                b=int(prices[2])        
                
                for i in range(n):
                    if topbrand==cars[i].TopBrands  and color == cars[i].color and cars[i].Price >= a and cars[i].Price <=b:
                        data={
                            'topbrand' : cars[i].TopBrands,
                            'model'    : cars[i].model,
                            'color': cars[i].color,
                            'price':cars[i].Price,
                            'img' :cars[i].img,
                            'url':cars[i].url,
                            }
                        brand.append(data)
                n1=len(brand)
            
                params={'lux':lux,'total':filtered,'length':n1,'top':top,'lens':top, 'range':range(nslides)  ,'filt':brand,}
                return render(request,'filterdata.html',params)
            
                # XX-- luxury and there atributes are on --xx

            elif topbrand =='no' and luxury != 'no' and color =='no' and price=='no':    
                for i in range(n2):
        
                    if luxury==cars2[i].Luxury:
                        data={
                            'Luxury' : cars2[i].Luxury,
                            'model'    : cars2[i].model,
                            'color': cars2[i].color,
                            'Price':cars2[i].Price,
                            'img' :cars2[i].img,
                            'url':cars2[i].url,
                            }
                        brands.append(data)
                n3=len(brands)
            
                params={'luxs':lux,'total':filtered,'lenss':n3,'top':top, 'range':range(nslides)  ,'filts':brands,}
                return render(request,'filterdata.html',params)
                # XX-- luxury and color combo -XX
            elif topbrand =='no' and luxury != 'no' and color !='no' and price=='no':    
                for i in range(n2):
                    if luxury==cars2[i].Luxury and color == cars2[i].color:
                        data={
                            'Luxury' : cars2[i].Luxury,
                            'model'    : cars2[i].model,
                            'color': cars2[i].color,
                            'Price':cars2[i].Price,
                            'img' :cars2[i].img,
                            'url':cars2[i].url,
                            }
                        brands.append(data)
                n3=len(brands)           
                params={'luxs':lux,'total':filtered,'lenss':n3,'top':top, 'range':range(nslides)  ,'filts':brands,}
                return render(request,'filterdata.html',params)
                #   XX-- luxury and price combo --XX
            elif topbrand =='no' and luxury != 'no' and color =='no' and price!='no':  
                prices =price.split()
                a=int(prices[0])
                b=int(prices[2])  
                for i in range(n2):
                    if luxury==cars2[i].Luxury and a<= cars2[i].Price <= b:
                        data={
                            'Luxury' : cars2[i].Luxury,
                            'model'    : cars2[i].model,
                            'color': cars2[i].color,
                            'Price':cars2[i].Price,
                            'img' :cars2[i].img,
                            'url':cars2[i].url,
                            }
                        brands.append(data)
                n3=len(brands)            
                params={'luxs':lux,'total':filtered,'lenss':n3,'top':top, 'range':range(nslides)  ,'filts':brands,}
                return render(request,'filterdata.html',params)
            elif topbrand =='no' and luxury != 'no' and color !='no' and price!='no':    
                prices =price.split()
                a=int(prices[0])
                b=int(prices[2]) 
                for i in range(n2):
                    if luxury==cars2[i].Luxury and color == cars2[i].color and a<= cars2[i].Price <= b:
                        data={
                            'Luxury' : cars2[i].Luxury,
                            'model'    : cars2[i].model,
                            'color': cars2[i].color,
                            'Price':cars2[i].Price,
                            'img' :cars2[i].img,
                            'url':cars2[i].url,
                            }
                        brands.append(data)
                n3=len(brands)            
                params={'luxs':lux,'total':filtered,'lenss':n3,'top':top, 'range':range(nslides)  ,'filts':brands,}
                return render(request,'filterdata.html',params)
                    # XX -- luxury and brands on --XX
            elif topbrand !='no' and luxury != 'no' and color =='no' and price=='no':
                for i in range(n):
                    if topbrand==cars[i].TopBrands:
                        data={
                            'topbrand' : cars[i].TopBrands,
                            'model'    : cars[i].model,
                            'color': cars[i].color,
                            'price':cars[i].Price,
                            'img' :cars[i].img,
                            'url':cars[i].url,
                            }
                        brand.append(data)
                n1=len(brand)
                for i in range(n2):
        
                    if luxury==cars2[i].Luxury:
                        data={
                            'Luxury' : cars2[i].Luxury,
                            'model'    : cars2[i].model,
                            'color': cars2[i].color,
                            'Price':cars2[i].Price,
                            'img' :cars2[i].img,
                            'url':cars2[i].url,
                            }
                        brands.append(data)
                   
                n3=len(brands)
            
                params={'luxs':lux,'total':filtered,'lens':n1,'lenss':n3,'top':top, 'range':range(nslides)  ,'filt':brand,'filts':brands}
                return render(request,'filterdata.html',params)

                # XX -- brand luxury and color is on -- XX

            elif topbrand !='no' and luxury != 'no' and color !='no' and price=='no':
                for i in range(n):
                    if topbrand==cars[i].TopBrands and color==cars[i].color:
                        data={
                            'topbrand' : cars[i].TopBrands,
                            'model'    : cars[i].model,
                            'color': cars[i].color,
                            'price':cars[i].Price,
                            'img' :cars[i].img,
                            'url':cars[i].url,
                            }
                        brand.append(data)
                n1=len(brand)
                for i in range(n2):
        
                    if luxury==cars2[i].Luxury and color==cars2[i].color:
                        data={
                            'Luxury' : cars2[i].Luxury,
                            'model'    : cars2[i].model,
                            'color': cars2[i].color,
                            'Price':cars2[i].Price,
                            'img' :cars2[i].img,
                            'url':cars2[i].url,
                            }
                        brands.append(data)
                   
                n3=len(brands)
            
                params={'luxs':lux,'total':filtered,'lens':n1,'lenss':n3,'top':top, 'range':range(nslides)  ,'filt':brand,'filts':brands}
                return render(request,'filterdata.html',params)

                # XX -- luxury price brand on --XX

            elif topbrand !='no' and luxury != 'no' and color =='no' and price!='no':
                prices =price.split()
                a=int(prices[0])
                b=int(prices[2])
                for i in range(n):
                    if topbrand==cars[i].TopBrands and a<= cars[i].Price <=b :
                        data={
                            'topbrand' : cars[i].TopBrands,
                            'model'    : cars[i].model,
                            'color': cars[i].color,
                            'price':cars[i].Price,
                            'img' :cars[i].img,
                            'url':cars[i].url,
                            }
                        brand.append(data)
                n1=len(brand)
                for i in range(n2):
        
                    if luxury==cars2[i].Luxury and a<= cars2[i].Price <=b:
                        data={
                            'Luxury' : cars2[i].Luxury,
                            'model'    : cars2[i].model,
                            'color': cars2[i].color,
                            'Price':cars2[i].Price,
                            'img' :cars2[i].img,
                            'url':cars2[i].url,
                            }
                        brands.append(data)
                   
                n3=len(brands)
            
                params={'luxs':lux,'total':filtered,'lens':n1,'lenss':n3,'top':top, 'range':range(nslides)  ,'filt':brand,'filts':brands}
                return render(request,'filterdata.html',params)

                    # XX -- Everything is on --XX 

            elif topbrand !='no' and luxury != 'no' and color !='no' and price!='no':
                prices =price.split()
                a=int(prices[0])
                b=int(prices[2])
                
                for i in range(n):
                    if topbrand==cars[i].TopBrands and color==cars[i].color and a<= cars[i].Price <=b:
                        data={
                            'topbrand' : cars[i].TopBrands,
                            'model'    : cars[i].model,
                            'color': cars[i].color,
                            'price':cars[i].Price,
                            'img' :cars[i].img,
                            'url':cars[i].url,
                            }
                        brand.append(data)
                n1=len(brand)
                for i in range(n2):
        
                    if luxury==cars2[i].Luxury and color==cars2[i].color and a<= cars2[i].Price <=b:
                        data={
                            'Luxury' : cars2[i].Luxury,
                            'model'    : cars2[i].model,
                            'color': cars2[i].color,
                            'Price':cars2[i].Price,
                            'img' :cars2[i].img,
                            'url':cars2[i].url,
                            }
                        brands.append(data)
                   
                n3=len(brands)
            
                params={'luxs':lux,'total':filtered,'lens':n1,'lenss':n3,'top':top, 'range':range(nslides)  ,'filt':brand,'filts':brands}
                return render(request,'filterdata.html',params)

                # XX-- only color is on --XX

            elif topbrand =='no' and luxury == 'no' and color !='no' and price=='no':

                for i in range(n):
                    if color==cars[i].color:
                        data={
                            'topbrand' : cars[i].TopBrands,
                            'model'    : cars[i].model,
                            'color': cars[i].color,
                            'price':cars[i].Price,
                            'img' :cars[i].img,
                            'url':cars[i].url,
                            }
                        brand.append(data)
          
                n1=len(brand)
                for i in range(n2):
        
                    if color==cars2[i].color:
                        data={
                            'Luxury' : cars2[i].Luxury,
                            'model'    : cars2[i].model,
                            'color': cars2[i].color,
                            'Price':cars2[i].Price,
                            'img' :cars2[i].img,
                            'url':cars2[i].url,
                            }
                        brands.append(data)
                  
                n3=len(brands)
            
                params={'luxs':lux,'total':filtered,'lens':n1,'lenss':n3,'top':top, 'range':range(nslides)  ,'filt':brand,'filts':brands}
                return render(request,'filterdata.html',params)

                # XX-- only price is on --XX
            elif topbrand =='no' and luxury == 'no' and color =='no' and price!='no':
                prices =price.split()
                a=int(prices[0])
                b=int(prices[2])

                for i in range(n):
                    if cars[i].Price >= a and cars[i].Price <=b:
                        data={
                            'topbrand' : cars[i].TopBrands,
                            'model'    : cars[i].model,
                            'color': cars[i].color,
                            'price':cars[i].Price,
                            'img' :cars[i].img,
                            'url':cars[i].url,
                            }
                        brand.append(data)
              
                n1=len(brand)
                for i in range(n2):
        
                    if cars2[i].Price >=a  and  cars2[i].Price <= b:
                        data={
                            'Luxury' : cars2[i].Luxury,
                            'model'    : cars2[i].model,
                            'color': cars2[i].color,
                            'Price':cars2[i].Price,
                            'img' :cars2[i].img,
                            'url':cars2[i].url,
                            }
                        brands.append(data)
            
                n3=len(brands)
            
                params={'luxs':lux,'total':filtered,'lens':n1,'lenss':n3,'top':top, 'range':range(nslides)  ,'filt':brand,'filts':brands}
                return render(request,'filterdata.html',params)

                # XX-- color and price on --XX
            elif topbrand =='no' and luxury == 'no' and color !='no' and price!='no':
                prices =price.split()
                a=int(prices[0])
                b=int(prices[2])
           
                for i in range(n):
                    if cars[i].color  == color and cars[i].Price >= a and cars[i].Price <=b:
                        data={
                            'topbrand' : cars[i].TopBrands,
                            'model'    : cars[i].model,
                            'color': cars[i].color,
                            'price':cars[i].Price,
                            'img' :cars[i].img,
                            'url':cars[i].url,
                            }
                        brand.append(data)
                  
                n1=len(brand)
                for i in range(n2):
        
                    if cars2[i].color == color   and cars2[i].Price >=a  and  cars2[i].Price <= b:
                        data={
                            'Luxury' : cars2[i].Luxury,
                            'model'    : cars2[i].model,
                            'color': cars2[i].color,
                            'Price':cars2[i].Price,
                            'img' :cars2[i].img,
                            'url':cars2[i].url,
                            }
                        brands.append(data)
              
                n3=len(brands)
            
                params={'luxs':lux,'total':filtered,'lens':n1,'lenss':n3,'top':top, 'range':range(nslides)  ,'filt':brand,'filts':brands}
                return render(request,'filterdata.html',params)
