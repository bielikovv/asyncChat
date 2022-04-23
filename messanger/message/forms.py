
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=150, label='Имя пользователя', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(max_length=32, label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(max_length=32, label='Подтвердите пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, label='Имя пользователя', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=32, label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User

# class ChangeProfile(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['username', 'usersurname', 'date_of_birth', 'photo']