from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    car=Car.objects.all()
    brand=Brand.objects.all()
    salon=Avtosalon.objects.all()
    context={
        "car":car,
        "brand":brand,
        "salon":salon
    }
    return render(request,"index.html",context=context)

def salonlar(request,pk):
    car=Car.objects.filter(salon_id=pk)
    brand=Brand.objects.all()
    salon=Avtosalon.objects.get(pk=pk)
    context={
        "car":car,
        "brand":brand,
        "salon":salon
    }
    return render(request,"salon.html",context=context)

def cars(request,pk):
    car=Car.objects.get(pk=pk)
    brand=Brand.objects.all()
    salon=Avtosalon.objects.all()
    context={
        "car":car,
        "brand":brand,
        "salon":salon
    }
    return render(request,"car.html",context=context)

def brands(request,pk):
    car=Car.objects.filter(brand_id=pk)
    brand=Brand.objects.get(pk=pk)
    context={
        "car":car,
        "brand":brand
    }
    return render(request,"brand.html",context=context)

def add_salons(request):
    if request.method =='POST':
        form=SalonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=SalonForm()

    return render(request,'add_salon.html',{"form":form})


def add_brands(request):
    if request.method=='POST':
        form=BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =BrandForm()

    return render(request,'add_brand.html',{"form":form})


def add_cars(request):
    if request.method=='POST':
        form=CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=CarForm()

    return render(request,'add_car.html',{"form":form})

