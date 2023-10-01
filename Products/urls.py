from django.urls import path
from Products.views import index,show,delete,create,edit,createbyform,editbyform
urlpatterns = [

    # path('show/', index, name='Products.home'),
    # path('<int:Product_id>', show, name='Products.show'),
    # path('<int:Product_id>/delete', delete, name='Products.delete')
    path('home/',index,name='Products.home'),
    path('<int:product_id>/',show,name='Products.show'),
    path('<int:product_id>/delete',delete,name='Products.delete'),
    path('create/',create,name='products.create'),
    path('edit/<int:product_id>/', edit, name='edit'),
    path('forms/create',createbyform,name='products.createform'),
    path('<int:id>/forms/edit',editbyform,name='products.editform'),
]