from django.shortcuts import render, get_object_or_404
from .models import Category, Product

    
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True) 
    query = request.GET.get('search')
    if query:
        products = products.filter(name__icontains=query)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        
    return render(request, 'tienda/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'query': query 
    })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request,
                  'tienda/product/detail.html',
                  {'product': product})