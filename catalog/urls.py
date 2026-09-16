
from django.urls import path
#from catalog.apps import CatalogConfig
from catalog.views import home
from catalog.views import contacts


#app_name = CatalogConfig.name
app_name = 'catalog'

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),

]
