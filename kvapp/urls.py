
from django.urls import path
from .views import *

app_name= 'kvapp'

urlpatterns = [
    path('',HomeView.as_view(),name='home' ),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('all-products/',AllProductsView.as_view(), name='all-products'),
    path('product/<slug:slug>/',ProductDetailsView.as_view(), name='productsdetails'),
    path( 'add-to-cart-<int:pro_id>/',AddToCartView.as_view(), name='addtocart' ),

]
