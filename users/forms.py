from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
