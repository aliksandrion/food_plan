from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('recipe/<int:recipe_id>/', view_recipe, name='view_recipe'),
    path('recipe/add_recipe/', add_recipe, name='add_recipe'),

]