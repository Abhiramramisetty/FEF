from random import random

from django.contrib.auth import login, authenticate
from django.http import HttpResponseNotAllowed
from django.shortcuts import render

# Create your views here.
from django.shortcuts import *
from .models import *

# views.py
from django.shortcuts import render, redirect
from .models import Details  # Import the Details model

def signup(request):
    if request.method == "POST":
        username = request.POST.get('nm')
        email = request.POST.get('mail')
        password = request.POST.get('pw')
        confirm_password = request.POST.get('cpw')

        # Create a Details object to store the user input
        det = Details(username=username, email=email, password=password, confirm_password=confirm_password)
        det.save()

        return redirect('signin')  #

    return render(request, 'signup.html')


# def signin(request):
#     return render(request,'signin.html')
def signin(request):
    username=request.POST.get('nm')
    password=request.POST.get('pw')
    print(username,password)
    user=authenticate(request,username=username, password=password)
    print(user)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return render(request,"signin.html")

def main(request):
    return render(request,"main.html")

def home(request):
    return render(request,"home.html")

def contactus(request):
    return render(request,"contactus.html")

def aboutus(request):
    return render(request,"aboutus.html")

def sell(request):
    return render(request,"sell.html")

def adoption(request):
    return render(request,"adoption.html")

def accessories(request):
    return render(request,"accessories.html")

def dogtip(request):
    return render(request,"dogtip.html")

def dogs(request):
    return render(request,"dogs.html")

def cats(request):
    return render(request,"cats.html")

def birds(request):
    return render(request,"birds.html")

def bulldog(request):
    return render(request,"bulldog.html")

def beagle(request):
    return render(request,"beagle.html")

def doberman(request):
    return render(request,"doberman.html")

def germanshephard(request):
    return render(request,"germanshephard.html")


def goldenretriever(request):
    return render(request, 'goldenretriever.html')

def husky(request):
    return render(request, 'husky.html')

def labrador(request):
    return render(request, 'labrador.html')

def pomeranian(request):
    return render(request, 'pomeranian.html')

def shiztzu(request):
    return render(request, 'shiztzu.html')

def ragdoll(request):
    return render(request,'ragdoll.html')

def siberian_cat(request):
    return render(request,'siberian_cat.html')

def persian_cat(request):
    return render(request,'persian_cat.html')

def bengal_cat(request):
    return render(request,'bengal_cat.html')

def peterbald(request):
    return render(request,'peterbald.html')

def himalayan(request):
    return render(request,'himalayan.html')

def parakeets(requets):
    return render(requets,"parakeets.html")

def cockatiel(request):
    return render(request,"cockatiel.html")

def dove(request):
    return render(request,"dove.html")

def canary(request):
    return render(request,"canary.html")

def hyacinth(request):
    return render(request,"hyacinth.html")

def lovebirds(request):
    return render(request,"lovebirds.html")
def acc_cat(request):
    return render(request,"acc_cat.html")

def acc_dog(request):
    return render(request,"acc_dog.html")

def acc_bird(request):
    return render(request,"acc_bird.html")

def payment(request):
    return render(request,"payment.html")

def success(request):
    return render(request,"success.html")

def cart(request):
    return render(request,"cart.html")


def receipt(request):
   return render(request,"receipt.html")