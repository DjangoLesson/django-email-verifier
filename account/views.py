from django.shortcuts import render
from django.views.generic import View
from django.utils import timezone
from django.http import HttpResponse
from . import forms
from . import utils
from . import models


class LoginView(View):

    def get(self, request):
        return render(request, 'account/login.html')


class RegistrationView(View):
    def get(self, request):
        form = forms.RegisterForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save_user()
            utils.send_activation_token(user)
            return render(request, 'account/pending.html')
        return render(request, 'account/register.html', {'form': form})


class TokenView(View):
    def get(self, request, token):
        user = models.User.objects.filter(token=token, is_verified=False).first()
        if user is not None and not user.is_token_expired:
            user.is_verified = True
            user.verified_date = timezone.now()
            user.save()
            return HttpResponse("Hisob aktivlashdi!")
        return HttpResponse("Invalid token.", status=400)
