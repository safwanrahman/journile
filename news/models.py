from django.db import models
from taggit.managers import TaggableManager

# Create your models here.


class Article(models.Model):
    formatted_text = models.TextField()
    plain_text = models.TextField()
    author = models.CharField(blank=True, max_length=50)
    categories = TaggableManager()
