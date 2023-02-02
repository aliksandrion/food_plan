from django import forms
from .models import Category


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=150, label='Name')
    ingredients = forms.CharField()
    directions = forms.CharField()
    photo = forms.ImageField()
    calories = forms.IntegerField(required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Choose category')
