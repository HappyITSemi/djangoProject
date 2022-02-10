#
from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import TemplateView

from .forms import SignupForm


def top(request):
    return render(request, 'accounts/login.html')


class LoginView(TemplateView):
    template_name = 'accounts/login.html'


class LogoutView(TemplateView):
    template_name = 'accounts/logout.html'


class PasswordChangeView(TemplateView):
    pass


class PasswordChangeDoneView(TemplateView):
    pass


class PasswordResetView(TemplateView):
    pass


class PasswordResetDoneView(TemplateView):
    pass


class PasswordResetConfirmView(TemplateView):
    pass


class PasswordResetCompleteView(TemplateView):
    pass


class SignupView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid


class ProfileUpdateView(TemplateView):
    pass
