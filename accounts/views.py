from django.shortcuts import render,reverse,redirect
from Products.models import product
from django.http import  HttpResponse

# Create your views here.


def profile(request):
    bact_to_url = reverse('Products.home')
    return redirect(bact_to_url)