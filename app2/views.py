from django.shortcuts import render,redirect
# from django.http import HttpResponse
from .models import *
from django.contrib import messages
from app2.form import CustomUserForm
# CustomUserForm

# Create your views here.

def home(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')

def register(request):
    form=CustomUserForm()
    if request.method=='POST':
       form=CustomUserForm(request.POST)
       if (form.is_valid()):
          form.save()
          messages.success(request,"Registration Success You Can Login Now" )
          return redirect('/login')
    return render(request,'register.html',{'form':form})

def collection(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request,'collection.html',{"catagory":catagory})

def collectionview(request,name):
   if(Catagory.objects.filter(name=name,status=0)):
         products=Product.objects.filter(catagory__name=name)
         return render(request,'productindex1.html',{"products":products,"catagory_name":name})

   else:
       messages.warning(request,"No Such Catagory Found")
    #    return rediect('collection')

def product_details(request,cname,pname):
     if(Catagory.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            products=Product.objects.filter(name=pname,status=0).first()
            return render(request,'productdetails.html',{'products':products})
        
         

















