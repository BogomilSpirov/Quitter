from django.contrib.auth import views as auth_views, login
from django.urls import reverse_lazy
from django.views import generic as views

from quitter.accounts.forms import RegisterUserForm, LoginUserForm


# Create your views here.


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginUserForm


class LogoutUserView(auth_views.LogoutView):
    ...
