from django.views import View
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from .forms import HomeForm


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'Login.html'


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'Signup.html'


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html', context={'is_staff': User.is_staff, 'form': HomeForm})


class MainView(View):
    def get(self, request):
        return render(request, 'main.html', context={})
