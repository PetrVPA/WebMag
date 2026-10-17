from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView
from users.forms import UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('home')

'''class LoginView(View):
    form_class = RegisterView
    template_name = 'login.html'

class Logout_view(View):
    form_class = RegisterView
    template_name = 'logout.html'
    success_url = reverse_lazy('home')'''
