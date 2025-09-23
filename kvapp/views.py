from django.shortcuts import render
from django.views.generic import TemplateView,DetailView
from .models import *
# Create your views here.



class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myname']= "Hadiuzzaman"
        context['product_list']= Product.objects.all().order_by('-id')
        return context

class AllProductsView(TemplateView):
    template_name = 'allproducts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allcategories'] = Category.objects.all()
        return context

class ProductDetailsView(TemplateView):
    template_name = 'productdetails.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        slug= kwargs['slug']
        product=Product.objects.get(slug=slug)
        product.view_count+=1
        product.save()
        context['product']= product
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

