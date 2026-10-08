from django.shortcuts import render, get_object_or_404

from catalog.models import Product



def home(request):
    return render(request, 'home.html')#папка template для файлов страниц программы по умолчанию и не указ

def contacts(request):
    return render(request, 'contacts.html')

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)



