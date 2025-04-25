from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import User

class HomeView(TemplateView):
    template_name = 'accounts/home.html'

class UserRegistrationView(CreateView):
    model = User
    template_name = 'accounts/register.html'
    fields = ['username', 'email', 'password', 'phone_number', 'address']
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        messages.success(self.request, 'Registration successful! Please login.')
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, f'Welcome back, {form.get_user().username}!')
        return super().form_valid(form)

class UserLogoutView(LogoutView):
    next_page = 'home'

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'You have been logged out.')
        return super().dispatch(request, *args, **kwargs)

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
    login_url = 'login' 