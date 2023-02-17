from django import forms
from .models import Recipes
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    subject = forms.CharField(label='Subject', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Text', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    captcha = CaptchaField()


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Enter password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ['title', 'ingredients', 'directions', 'photo', 'calories', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'directions': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

    def clean_title(self):
        title = self.cleaned_data(['title'])
        if re.match(r'/d', title):
            raise ValidationError("Name must begin with a letter")
        return title
