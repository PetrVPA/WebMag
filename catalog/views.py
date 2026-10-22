from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy

from catalog.forms import ProductForm
from catalog.models import Product
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .services import get_product_from_cache



class ProductListView(ListView):
    model = Product
    template_name = 'product_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

    def get_queryset(self):
        return get_product_from_cache()


class ProductContactView(ListView):
    model = Product
    template_name = 'contacts.html'


@method_decorator(cache_page(60*15), name='dispatch')
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

    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('catalog.can_create_product'):
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("У вас нет прав на создание продукта.")


class ProductUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = 'catalog.can_edit_product'
    model = Product
    form_class = ProductForm
    template_name = 'product_edit.html'
    success_url = reverse_lazy('catalog:product_start')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        has_edit_perm = request.user.has_perm('catalog.can_edit_product')
        if request.user == product.owner or has_edit_perm:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("Вы не являетесь владельцем этого продукта или модератором.")


class ProductDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = 'catalog.can_delete_product'
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('catalog:product_start')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        has_edit_perm = request.user.has_perm('catalog.can_delete_product')
        if request.user == product.owner or has_edit_perm:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("Вы не являетесь владельцем этого продукта или модератором.")


