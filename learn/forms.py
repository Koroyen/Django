from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        'class': 'w-full px-4 py-2 rounded bg-black text-white border border-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500'
    }))

    class Meta:
        model = CustomUser
        fields = ('email', 'password')