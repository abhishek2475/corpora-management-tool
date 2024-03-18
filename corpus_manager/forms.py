# Necessary imports
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import ParallelText

class CustomSignupForm(UserCreationForm):
    """
    A custom form for user signup.

    Inherits from UserCreationForm and adds additional fields for email and role.
    """

    # Additional field for email
    email = forms.EmailField()

    # Choices for the role field
    role_choices = [
        ('Data Manager', 'Data Manager'),
        ('Translator', 'Translator'),
        ('Validator', 'Validator'),
    ]

    # Field for selecting the role
    role = forms.ChoiceField(choices=role_choices)

    class Meta:
        # Specify the model to be used for the form
        model = User
        
        # Specify the fields to be included in the form
        fields = ["username", "email", "password1", "password2"]

class ParallelTextForm(forms.ModelForm):
    """
    A form for creating and updating parallel texts.

    Inherits from ModelForm and specifies the model and fields to be used.
    """

    class Meta:
        # Specify the model to be used for the form
        model = ParallelText

        # Specify the fields to be included in the form
        fields = ['en_text', 'hi_text', 'mn_text', 'verify_en_mn', 'verify_hi_mn', 'verify_en_hi']

class FilterForm(forms.Form):
    """
    A form for filtering parallel texts.

    Provides choices for source and target languages.
    """

    # Choices for source and target languages
    choices = [
        ('en', 'English'),
        ('hi', 'Hindi'),
        ('mn', 'Manipuri')
    ]
    # Field for selecting the source language
    source = forms.ChoiceField(choices=choices)
    # Field for selecting the target language
    target = forms.ChoiceField(choices=choices)
