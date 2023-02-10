from django.contrib import admin
from .models import Recipes, Category


class NewsAdmin(admin.ModelAdmin):
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
