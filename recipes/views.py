from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from .models import Recipes, Category
from .forms import RecipeForm


class HomeRecipe(ListView):
    model = Recipes
    template_name = 'recipes/home_recipes_list.html'
    context_object_name = 'recipes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        return context


class CategoryRecipe(ListView):
    model = Recipes
    template_name = 'recipes/category.html'
    context_object_name = 'recipes'
    allow_empty = False

    def get_queryset(self):
        return Recipes.objects.filter(category_id=self.kwargs['category_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


class ViewRecipe(DetailView):
    model = Recipes
    context_object_name = 'recipe_item'


def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            new_recipe = form.save()
            return redirect(new_recipe)
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})
