from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Contact, Review
from .forms import ContactForm, ReviewForm
from django.contrib import messages


def product_list(request, category_slug=None):
    
    category = None
    categories = Product.objects.all()
    products = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Product, slug=category_slug)
        products = products.filter(category=category)
        
    context = {'category': category, 'categories': categories, 'products': products}
    return render(request, 'shop/product/list.html', context)

def product_detail(request, id, slug):
    
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})



def new_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop:contact_success')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'shop/product/contact.html', context)

def contact_success(request):
    return render(request, 'shop/product/contact_success.html')


def reviews(request):
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop:display_reviews') 

    return render(request, 'shop/product/reviews.html', {'form': form, 'reviews': reviews})

def display_reviews(request):
    reviews = Review.objects.all() 
    return render(request, 'shop/product/display_reviews.html', {'reviews': reviews})
