from django.urls import path
from catalog.views import (ProductListView, ProductContactView, ProductDetailView,
                           ProductCreateView, ProductUpdateView, ProductDeleteView, ProductCategoryListView,
                           CategoryListView)
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page

app_name = 'catalog'

urlpatterns = [
    path("", ProductListView.as_view(), name='product_start'),#пути в адресной строке
    path("home/", ProductListView.as_view(), name='home'),
    path("contacts/", ProductContactView.as_view(), name='contacts'),
    path('home/<int:pk>/', cache_page(60)(ProductDetailView.as_view()) , name='product_detail'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('home/product_create/', ProductCreateView.as_view(), name='product_create'),
    path('home/product_edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('home/product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    path('list_category/', CategoryListView.as_view(), name='category_list'),

    # Страница категории по ID. Обратите внимание на <int:category_pk>
    path('category_detail/<int:category_pk>/', ProductCategoryListView.as_view(), name='category_detail'),


]
# Добавление статических маршрутов для медиафайлов
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)