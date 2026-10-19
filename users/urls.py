from django.contrib.auth.views import LoginView, LogoutView
from users.views import RegisterView
from django.urls import path

from users.apps import UsersConfig

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    #path('login/', LoginView.as_view(next_page='home'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    #path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
