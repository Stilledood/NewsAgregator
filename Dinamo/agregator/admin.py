from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    '''Class to construct a custom article admin class'''

    list_display = ['title','publishing_site','publishing_date']
    date_hierarchy = 'publishing_date'
    list_filter = ('publishing_date',)
    search_fields = ('title','publishing_site')

