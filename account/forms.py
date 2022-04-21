from django import forms
from django.core.exceptions import ValidationError
from account.models import User



class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email allaqachon qo\'shilgan!!!')
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('Username allaqachon qo\'shilgan!!!')
        return username
    
    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise ValidationError("Parolar mos kelmadi!!!")
        return confirm_password

    def save_user(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        user = User.objects.create(
            username=username, email=email
        )
        password = self.cleaned_data['password']
        user.set_password(password)
        user.save()
        return user
