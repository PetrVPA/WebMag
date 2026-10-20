from django.forms import ModelForm
from catalog.models import Product
from django.core.exceptions import ValidationError
import re


FORBIDDEN_WORDS = (
    "казино",
    "биржа",
    "обман",
    "криптовалюта",
    "дешево",
    "полиция",
    "крипта",
    "бесплатно",
    "радар",
)

MAX_IMAGE_SIZE = 5 * 1024 * 1024


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ("updated_at",)


    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is None:
            raise ValidationError("Укажите стоимость товара.")
        if price <= 0:
            raise ValidationError("Стоимость должна быть больше нуля.")
        return price

    def clean_images(self):
        image = self.cleaned_data.get("images")
        if image and image.size > MAX_IMAGE_SIZE:
            raise ValidationError("Размер изображения не должен превышать 5 МБ.")
        return image

    def clean(self):
        cleaned_data = super().clean()

        for field_name, label in (
            ("title", "названии продукта"),
            ("description", "описании продукта"),
        ):
            value = cleaned_data.get(field_name) or ""
            for word in FORBIDDEN_WORDS:
                if re.search(rf"\b{re.escape(word)}\b", value, re.IGNORECASE):
                    self.add_error(
                        field_name,
                        f"Слово «{word}» недопустимо в {label}.",
                    )

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

        self.fields["title"].widget.attrs["placeholder"] = (
            "Введите название продукта"
        )
        self.fields["description"].widget.attrs["placeholder"] = (
            "Введите описание"
        )
        self.fields["price"].widget.attrs["placeholder"] = (
            "Введите стоимость"
        )
        self.fields["images"].widget.attrs["accept"] = "image/jpeg,image/png"
        self.fields["created_at"].widget.attrs["type"] = "date"

    def clean_published_at(self):
        published_at = self.cleaned_data.get("published_at")

        return published_at

    class Meta:
        model = Product
        fields = ['title', 'description', 'images', 'category', 'price', 'created_at', 'updated_at', 'published_at',] # или как называется ваше поле

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем класс form-check-input для Bootstrap
        self.fields['published_at'].widget.attrs.update({
            'class': 'form-check-input'
        })





