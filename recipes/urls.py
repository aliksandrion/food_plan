from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', HomeRecipe.as_view(), name='home'),
    path('category/<int:category_id>/', CategoryRecipe.as_view(), name='category'),
    path('recipe/<int:pk>/', ViewRecipe.as_view(), name='view_recipe'),
    path('recipe/add_recipe/', CreateRecipe.as_view(), name='add_recipe'),
]