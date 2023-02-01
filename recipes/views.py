from django.shortcuts import render, get_object_or_404

from .models import Recipes, Category


def index(request):
    recipes = Recipes.objects.all()
    context = {
        'recipes': recipes,
        'title': 'Recipes',
    }
    return render(request, template_name='recipes/index.html', context=context)


def get_category(request, category_id):
    recipes = Recipes.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'recipes/category.html', {'recipes': recipes, 'category': category})


def view_recipe(request, recipe_id):
    # recipe_item = Recipes.objects.get(pk=recipe_id)
    recipe_item = get_object_or_404(Recipes, pk=recipe_id)
    return render(request, 'recipes/view_recipe.html', {"recipe_item": recipe_item})
