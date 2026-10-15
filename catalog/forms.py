from django.forms import ModelForm
from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        #fields = ['title', 'description', 'price', 'image', 'category', 'created_at']
        exclude = ('updated_at',)
