import email
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms

from .models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["username", "password"]


class RegistrationUserForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя")
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")
        labels = {
            "email": "Почтовый ящик",
            "first_name": "Имя",
            "last_name": "Фамилия",
        }

    # def clean_email(self):
    #     email = self.cleaned_data["email"]
    #     if get_user_model().objects.filter(email=email).exists():
    #          raise forms.ValidationError("This Email already exists!")
    #     return email
    

class ProfileForm(UserChangeForm):
    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "image"]