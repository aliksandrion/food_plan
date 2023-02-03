from django import forms
from .models import Recipes
import re
from django.core.exceptions import ValidationError


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
