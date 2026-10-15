from django.contrib import admin

from blog.models import Blog



# Register your models here.
@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_article', 'content', 'preview', 'created_at', 'publication_indicator', 'number_views')
    list_editable = ('publication_indicator','title_article','content',)

    search_fields = ('id', 'publication_indicator',)

