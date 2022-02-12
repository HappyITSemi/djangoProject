from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import TemplateView

from .forms import SignupForm


def home(request):
    return render(request, "auth/login.html")


def top(request):
    return render(request, 'auth/login.html')


class LoginView(TemplateView):
    template_name = 'auth/login.html'


class LogoutView(TemplateView):
    template_name = 'auth/logout.html'


class PasswordChangeView(TemplateView):
    template_name = 'auth/password_change_form.html'
    success_url = reverse_lazy('auth:password_change_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # 継承元のメソッドCALL
        context["form_name"] = "password_change"
        return context


class PasswordChangeDoneView(TemplateView):
    template_name = 'auth/password_change_done.html'


class PasswordResetView(TemplateView):
    template_name = 'auth/password_reset_form.html'
    subject_template_name = 'auth/mail_template/reset/subject.txt'
    email_template_name = 'auth/mail_template/reset/message.txt'
    success_url = reverse_lazy('auth:password_reset_done')


class PasswordResetDoneView(TemplateView):
    template_name = 'auth/password_reset_done.html'


class PasswordResetConfirmView(TemplateView):
    template_name = 'auth/password_reset_confirm.html'
    success_url = reverse_lazy('auth:password_reset_complete')


class PasswordResetCompleteView(TemplateView):
    template_name = 'auth/password_reset_complete.html'


class SignupView(CreateView):
    template_name = 'auth/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid


class SignupClosed(TemplateView):
    template_name = 'auth/signup_closed.html'


class VerificationSent(TemplateView):
    template_name = 'accounts/verification_sent.html'


class VerifiedEmailRequired():
    template_name = 'verified_email?required.html'


class ProfileUpdateView(TemplateView):
    pass
