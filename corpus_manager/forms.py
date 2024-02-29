from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import ParallelText

class CustomSignupForm(UserCreationForm):
    email = forms.EmailField()
    role_choices = [
        ('Data Manager', 'Data Manager'),
        ('Translator', 'Translator'),
        ('Validator', 'Validator'),
    ]
    role = forms.ChoiceField(choices=role_choices)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class LoginForm(AuthenticationForm):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your email",
                "class": "w-full py-2 px-6 rounded-xl",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "w-full py-2 px-6 rounded-xl"}
        )
    )

class ParallelTextForm(forms.ModelForm):
    class Meta:
        model = ParallelText
        fields = ['source_text', 'target_text', 'verification1', 'verification2', 'verification3', 'verification4', 'verification5']
