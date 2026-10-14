from django.shortcuts import render, get_object_or_404
from catalog.models import Product
from django.views.generic import ListView, DetailView


class ProductListView(ListView):
    model = Product
    template_name = 'product_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

#def home(request):
    #products = Product.objects.all()
    #context = {'products': products}
    #return render(request, 'product_base.html', context)#папка template для файлов страниц программы по умолчанию и не указ

class ProductContactView(ListView):
    model = Product
    template_name = 'contacts.html'

#def contacts(request):
    #return render(request, 'contacts.html')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


#def product_detail(request, pk):
    #product = get_object_or_404(Product, pk=pk)
    #context = {'product': product}
    #return render(request, 'product_detail.html', context)



