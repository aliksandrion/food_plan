from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipes, Category
from .forms import RecipeForm


class HomeRecipe(ListView):
    model = Recipes
    template_name = 'recipes/home_recipes_list.html'
    context_object_name = 'recipes'
    queryset = Recipes.objects.select_related('category')
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        return context


class CategoryRecipe(ListView):
    model = Recipes
    template_name = 'recipes/category.html'
    context_object_name = 'recipes'
    allow_empty = False
    paginate_by = 5

    def get_queryset(self):
        return Recipes.objects.filter(category_id=self.kwargs['category_id']).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


class ViewRecipe(DetailView):
    model = Recipes
    context_object_name = 'recipe_item'


class CreateRecipe(LoginRequiredMixin, CreateView):
    form_class = RecipeForm
    template_name = 'recipes/add_recipe.html'
    login_url = '/admin/'
