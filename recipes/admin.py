from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from django import forms
from .models import Recipes, Category


class RecipesAdminForm(forms.ModelForm):
    ingredients = forms.CharField(widget=CKEditorUploadingWidget())
    directions = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Recipes
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = RecipesAdminForm
    list_display = ('id', 'title', 'category', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'directions')
    list_filter = ('category',)
    fields = ('title', 'ingredients', 'directions', 'photo', 'calories', 'category', 'created_at')
    readonly_fields = ('created_at',)
    save_on_top = True


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Recipes, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Change recipes'
admin.site.site_header = 'Change recipes'
