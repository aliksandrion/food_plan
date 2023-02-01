from django.db import models
from django.urls import reverse


class Recipes(models.Model):
    title = models.CharField(max_length=150, verbose_name='Name of the dish')
    ingredients = models.TextField(verbose_name='Ingredients')
    directions = models.TextField(verbose_name='Directions')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo', blank=True)
    calories = models.IntegerField(default=0, verbose_name='Calories')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Category')

    def get_absolute_url(self):
        return reverse('view_recipe', kwargs={"recipe_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
        ordering = ['-created_at']


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Category')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']
