from django.contrib import admin
from .models import WebMain


@admin.register(WebMain)
# Configure administration of WebMain model.
# Nastavuje administraci WebMain modelu.
class WebMain(admin.ModelAdmin):
    list_display = (
        'article_code',
        'article_sequence',
        'aticle_content'
    )
    list_filter = ('article_code', 'article_sequence')
    search_fields = ('article_code', 'article_sequence')
    ordering = ('article_sequence','article_code')
