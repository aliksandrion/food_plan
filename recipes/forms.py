from django import forms
from .models import Recipes


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
    # title = forms.CharField(max_length=150, label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # ingredients = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    # directions = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    # photo = forms.ImageField()
    # calories = forms.IntegerField(required=False)
    # category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Select a category',
    #                                   widget=forms.Select(attrs={'class': 'form-control'}))
