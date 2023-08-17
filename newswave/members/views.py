from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib import messages

from .forms import NewUserForm


class UserRegisterView(CreateView):
    template_name = "registration/register.html"

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)

    def post(self, *args, **kwargs):
        password_mismatch = False
        form = NewUserForm(self.request.POST)
        username = self.request.POST.get("username")
        email = self.request.POST.get("email")
        if form.is_valid():
            form.save()
            messages.success(self.request, "Registration successful." )
            return redirect("login")
        else:
            password_mismatch = True
        
        register = {"password_mismatch": password_mismatch, "username": username, "email": email}
        
        return render(self.request, self.template_name, register)
