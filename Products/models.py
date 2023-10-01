from django.db import models
from django.shortcuts import  reverse
# Create your models here.
class catigory(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    @classmethod
    def get_all_catigories(cls):
        return cls.objects.all()
    @classmethod
    def get_specific_catigory(cls,id):
        return cls.objects.get(id=id)

class product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0, null=True)
    image = models.ImageField(upload_to='products/images/',default='l1.jpg')
    catigory=models.ForeignKey(catigory, null=True,blank=True,on_delete=models.CASCADE,related_name='other')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    # in_stock = models.BooleanField(default=True)
    # description =models.TextField(null=True)
    # no_of_items =models.IntegerField(default=10)
    # color=models.CharField(default='black',max_length=10)
    def __str__(self):
        return self.name

    @classmethod
    def get_all_products(cls):
        return cls.objects.all()
    @classmethod
    def get_specific_product(cls,name):
        return cls.objects.get(name=name)

    def get_image_url(self):
        return f'/media/{self.image}'
    def get_edit_url(self):
        return reverse('products.editform',args=[self.id])