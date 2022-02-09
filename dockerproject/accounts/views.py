from django.contrib.auth.models import User
from django.shortcuts import render

from accounts.forms import CustomUserChangeForm


def home(request):
    return render(request, "accounts/home.html")


def edit(request, pk):
    target_user = User.objects.filter(id=pk).first()
    if request.method == "GET":
        form = CustomUserChangeForm(instance=target_user)
        return render(request, "accounts/edit.html", {"target_user": target_user})
    elif request.method == POST:
        form = CustomUserChangeForm(request.POST, instance=target_user)
        if form.is_valid:
            form.save()
            return render(request, "home.html")
        else:
            return render(request, "accounts/edit.html", {"target_user": target_user})
