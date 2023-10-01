from django.shortcuts import render,redirect, reverse
from Products.models import product,catigory
from Products.forms import productModelForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

products=[
        {'id':1,'name':'laptop','price':300,'img':'l1.jpg'},
        {'id':2,'name':'phone','price':300,'img':'p3.jpg'},
        {'id':3,'name':'haedphone','price':300,'img':'h1.jpg'},
        {'id':4,'name':'haedphone','price':300,'img':'h2.jpg'}
    ]

# def home(request):

#     return render(request,template_name='products/home.html',context={"name":"laptop","products":products})

def index(request):
    products = product.objects.all()
    pproduct=product.objects.order_by('id').first()
    return render(request, template_name='products/home.html', context={"products": products, "product": pproduct})

def show(request, product_id):
    product_obj = product.objects.get(id=product_id)
    return render(request, 'products/show.html', {'product': product_obj})

@login_required
def delete(request, product_id):
    product_ogj = product.objects.get(id=product_id)
    product_ogj.delete()
    bact_to_url = reverse('Products.home')
    return redirect(bact_to_url)
@login_required
def edit(request, product_id):
    producct = product.objects.get(id=product_id)
    if request.method == 'POST':
        producct.name = request.POST.get('name')
        producct.image = request.FILES.get('image')
        producct.price = request.POST.get('price')
        catigorry=None
        if 'catigory_id' in request.POST:
            catigorry=catigory.get_specific_catigory(request.POST['catigory_id'])
        producct.catigory=catigorry
        producct.save()
        bact_to_url = reverse('Products.home')
        return redirect(bact_to_url)
    catigories=catigory.get_all_catigories()
    return render(request, 'products/edit.html', {'product': producct,"catigories":catigories})
@login_required
def create(request):
    if request.method =='POST':
        request_data=request.POST
        request_image=request.FILES
        name=request_data['name']
        image=request_image['image']
        price=request_data['price']
        catigorry=None
        if 'catigory_id' in request.POST:
            catigorry=catigory.get_specific_catigory(request.POST['catigory_id'])
        product_cr=product(name=name,image=image,price=price,catigory=catigorry)
        product_cr.save()
        bact_to_url = reverse('Products.home')
        return redirect(bact_to_url)
    catigories=catigory.get_all_catigories()
    return render(request,template_name='products/create.html',context={"catigories":catigories})
@login_required
def createbyform(request):
     form  = productModelForm()
     if request.method == 'POST':
        form  = productModelForm( request.POST, request.FILES)
        if form.is_valid():
            form.save()
            url = reverse('Products.home')
            return redirect(url)

        return render(request, 'Products/createusingform.html', context={"form": form})


     return render(request, 'Products/createusingform.html', context={"form":form})
def editbyform(request):
    producct = product.objects.get(id)
    form = productModelForm(instance=producct)

    return render(request, 'Products/editusingform.html', context={"form": form, "image":product.get_image_url})