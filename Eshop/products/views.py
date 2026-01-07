from django.shortcuts import render
from .models import Product

# Create your views here.

def productView(request):
    template = 'product/product.html'
    context = {
        'products': Product.objects.all(),
        'current_page' : 'products'
        
    }
    return render(request, template_name= template, context=context)