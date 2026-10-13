from IPython.utils.PyColorize import pride_theme
from django.urls import path
from . import views
from catalog.views import ProductListView, ProductContactView, ProductDetailView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'catalog'

urlpatterns = [
    path("", ProductListView.as_view(), name='product_start'),#пути в адресной строке
    path("home/", ProductListView.as_view()),
    path("contacts/", ProductContactView.as_view()),
    path('home/<int:pk>/', ProductDetailView.as_view() , name='product_detail'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

]
# Добавление статических маршрутов для медиафайлов
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)