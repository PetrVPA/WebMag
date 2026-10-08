from IPython.utils.PyColorize import pride_theme
from django.urls import path
from . import views
from catalog.views import product_detail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home),#пути в адресной строке
    path("home/", views.home),
    path("contacts/", views.contacts),
    path('home/<int:id>/', product_detail, name='product_detail'),
    path('<int:id>/', product_detail, name='product_detail'),

]
# Добавление статических маршрутов для медиафайлов
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)