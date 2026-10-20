from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render

from catalog.forms import ProductForm
from catalog.models import Product
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class ProductListView(ListView):
    model = Product
    template_name = 'product_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class ProductContactView(ListView):
    model = Product
    template_name = 'contacts.html'


class ProductDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    permission_required = 'catalog.can_view_product'
    model = Product
    template_name = 'product_detail.html'


class ProductCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = 'catalog.can_create_product'
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('catalog:product_start')

    def form_valid(self, form):
        # commit=False создает объект, но не сохраняет в БД
        product = form.save(commit=False)
        # Привязываем текущего авторизованного пользователя
        product.owner = self.request.user
        # Теперь сохраняем в БД
        product.save()
        return super().form_valid(form)


class ProductUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = 'catalog.can_edit_product'
    model = Product
    form_class = ProductForm
    template_name = 'product_edit.html'
    success_url = reverse_lazy('catalog:product_start')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if request.user == product.owner or request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("Вы не являетесь владельцем этого продукта или модератором.")


class ProductDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = 'catalog.can_delete_product'
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('catalog:product_start')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if request.user == product.owner or request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("Вы не являетесь владельцем этого продукта или модератором.")