from django.shortcuts import render ,redirect,reverse
from django.http import HttpResponse
# Create your views here.
def home_page(request):
    return render(request,template_name='lab1/home.html')

def about(request):
    return render(request,template_name='lab1/about_us.html')

def contact_us(request):
    return render(request,template_name='lab1/contanct_us.html')


