from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    salon=Avtosalon.objects.all()
    context={
        "salon":salon
    }
    return render(request,"index.html",context=context)

def salonlar(request,pk):
    salon=Avtosalon.objects.get(pk=pk)
    brand=Brand.objects.all()
    context={
        "salon":salon,
        "brand":brand
    }
    return render(request,"salon.html",context=context)

def brands(request, salon, brand):
    salon_obj = Avtosalon.objects.get(pk=salon)
    brand_obj = Brand.objects.get(pk=brand)
    cars = Car.objects.filter(salon=salon_obj, brand=brand_obj)

    context = {
        'salon': salon_obj,
        'brand': brand_obj,
        'car': cars,
        'brands': Brand.objects.all(),  # Agar sidebarda barcha brandlar bo‘lsa
    }

    return render(request, 'brand.html', context)


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

