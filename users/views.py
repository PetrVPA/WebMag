from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic.edit import CreateView
from users.forms import UserRegisterForm
from django.core.mail import send_mail
from django.conf import settings

from_email = settings.DEFAULT_FROM_EMAIL

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)
