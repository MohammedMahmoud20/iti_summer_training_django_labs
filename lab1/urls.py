from django.urls import path
from lab1 import views

urlpatterns = [
    path('',views.home_page,name='home'),
    path('about/',views.about,name='about_us'),
    path('contact_us/',views.contact_us,name='contact_us'),
]

