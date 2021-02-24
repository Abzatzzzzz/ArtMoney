from django.contrib import admin
from .models import *


class YearAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class MonthAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'year')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', )


class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('money', 'category', 'month', 'description')


class TranshMvfAdmin(admin.ModelAdmin):
    list_display = ('money', 'category', 'month', 'description')


# class PostAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("title",)}
#     form = PostAdminForm
#     list_display = ('id', 'title', 'slug', 'category', 'created_at')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)
#     list_filter = ('category', 'tag')

admin.site.register(Expenses, ExpensesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Month, MonthAdmin)
admin.site.register(Year, YearAdmin)
admin.site.register(TranshMvf, TranshMvfAdmin)
