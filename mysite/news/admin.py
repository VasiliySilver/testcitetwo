from django.contrib import admin

from .models import News, Category

# добавим больше информации в админке новостей
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content') # добаляем поис по title, content
    list_editable = ('is_published',) # проверяей опубликовано или нет в виде чекбокса
    list_filter = ('is_published', 'category') # сортирует по публикации
# сначала всегда основная модель потом class

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)



