from django.shortcuts import render
from .models import Product

# Create your views here.

def productView(request):
    template = 'products/products.html'
    context = {
        'products': Product.objects.all(),
        'current_page' : 'products'
        
    }
    return render(request, template_name= template, context=context)

# search products
from django.db.models import Q
def searchProducts(request):
    
    template = 'products/search_results.html' 
    query = request.GET.get('query_text')
    if query:
        search_results = Product.objects.filter (
            Q(title__icontains = query) |
            Q(desc__icontains = query)
        )
        context = {
            'query' : query,
            'products' : search_results
        }
    return render(request, template_name= template, context=context)

# CRUD Operations using Generic Class Based Views of Django

from django.views.generic import (CreateView,DetailView,
                                  UpdateView,DeleteView,)

# ListView has already been implemented using a function a function above : producstView()

class CreateProduct(CreateView):
    model = Product
    template_name = 'products/add_product.html'
    fields = '__all__'
    # redirection url for successful creation of resource
    success_url = '/'

class AddProductImage(CreateView):
    model = Product
    template_name = "products/add_images.html"
    fields = "__all__"
    
    success_url = '/'

class ProductDetail(DetailView):
     model = Product
     template_name = 'products/product_details.html'
     context_object_name = 'product'
     
    #  overriding the quey\ryset to pre-fetch and the product images alongside produucts
    
     def get_queryset(self):
        return Product.objects.prefetch_related('images')
     
    

class UpdateProduct(UpdateView):
     model = Product
     template_name = 'products/update_product.html'
     fields = '__all__'
     success_url = '/'
    

class DeleteProduct(DeleteView):
     model = Product
     template_name = 'products/delete_product.html'
     fields = '__all__'
     success_url = '/'
    
    

# chat gpt code
from django.shortcuts import get_object_or_404, redirect
from .models import Product, ProductImage
from .forms import ProductImageForm

def add_product_image(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductImageForm(request.POST, request.FILES)
        if form.is_valid():
            media = form.save(commit=False)
            media.product = product
            media.save()
            return redirect('product_details', pk=pk)
    else:
        form = ProductImageForm()

    return render(
        request,
        'products/add_images.html',
        {
            'form': form,
            'product': product
        }
    )
