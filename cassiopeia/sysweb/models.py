
from django.conf import settings
from django.db import models
from django.utils import timezone

# Stores content for the Whohas home page.
# Ukládá obsah úvodní stránky Whohas.
class WebMain(models.Model):
     article_code = models.CharField(max_length=24, null=True)
     article_sequence = models.PositiveIntegerField(null=False)
     aticle_content = models.TextField(null=True)