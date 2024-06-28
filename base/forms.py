from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Task

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField(max_length=255)

    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'password1', 'password2')

class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6, required=True)

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']