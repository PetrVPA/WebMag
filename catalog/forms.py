from django.forms import ModelForm
from catalog.models import Product
from django.core.exceptions import ValidationError
import re


class ProductForm(ModelForm):
    class Meta:
        model = Product
        #fields = ['title', 'description', 'price', 'image', 'category', 'created_at']
        exclude = ('updated_at',)


    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise ValidationError('Стоимость болжна быть больше 0')
        return price

    def clean(self):
        cenzor = ['казино', 'биржа', 'обман', 'криптовалюта', 'дешево', 'полиция', 'крипта', 'бесплатно', 'радар']
        cleaned_data = super().clean()

        text_title =cleaned_data.get ('title')
        for word in cenzor:
            if (re.search(r'\b{}\b'.format(re.escape(word)), text_title, re.IGNORECASE)):
                self.add_error('title','- Это не допустимое слово в названии продукта')

        text_description = self.cleaned_data['description']

        for word in cenzor:
            if (re.search(r'\b{}\b'.format(re.escape(word)), text_description, re.IGNORECASE)):
                self.add_error('description','- Это не допустимое слово в описании продукта')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        # Настройка атрибутов виджета для поля 'title'
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите название продукта'  # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'description'
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите описание'  # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'price'
        self.fields['price'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите стоимость'  # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'image'

        self.fields['images'].widget.attrs.update({'class': 'form-control', 'type': 'foto'})

        # Настройка атрибутов виджета для поля 'category'
        self.fields['category'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Выберите категорию'  # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'created_at'
        self.fields['created_at'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'type': 'date'  # Указание типа поля как даты
        })





