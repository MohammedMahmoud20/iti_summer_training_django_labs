from django import forms
from Products.models import catigory,product
# class productsform(forms.Form):
#     name=forms.CharField(label="name",max_length=100)
#     price=forms.IntegerField(label="price")
#     image=forms.ImageField(label="image")
#     catigorry_id=forms.ModelChoiceField(queryset=catigory.objects.all(),label="catigory")



class productModelForm(forms.ModelForm):
    class Meta:
        model = product
        fields = '__all__'

