
from django.urls import path
from .views import HomeView,AboutView,ContactView, AllProductsView,ProductDetailsView

app_name= 'kvapp'

urlpatterns = [
    path('',HomeView.as_view(),name='home' ),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('all-products/',AllProductsView.as_view(), name='all-products'),
    path('product/<slug:slug>/',ProductDetailsView.as_view(), name='productsdetails'),

]
