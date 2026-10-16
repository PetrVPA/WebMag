from django.contrib.auth.forms import UserCreationForm
from django import forms


class StyleFormMixin:
    pass


from users.forms import StyleFormMixin
from users.models import User



class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Phone number must contain only digits.')
        return phone_number