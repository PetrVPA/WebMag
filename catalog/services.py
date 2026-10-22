from django.core.cache import cache
from django.shortcuts import get_object_or_404

from config.settings import CACHE_ENABLED
from .models import Product, Category


def get_product_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_products_by_category(category_identifier):
    """
    Сервисная функция для получения списка всех продуктов в указанной категории.

    Принимает:
        category_identifier (str | int): Slug или ID категории.

    Возвращает:
        QuerySet: Список продуктов.
    """
    # Проверяем, что категория вообще существует (опционально, но полезно)
    # Мы можем искать по slug или по id
    category = get_object_or_404(Category, pk=category_identifier)

    # Возвращаем продукты.
    # Используем select_related('category'), чтобы избежать N+1 запросов,
    # если в шаблоне мы будем выводить название категории у каждого продукта.
    return Product.objects.filter(category=category).select_related('category')
