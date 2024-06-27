from django.db import models
from datetime import timedelta, timezone
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=300)
    bio = models.TextField()

    def __str__(self):
        return f"{self.name}"
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f"{self.title} - {self.published_date}"

    def published_recently(self):
        return self.published_date >= timezone.now() - timedelta(days=7)

    published_recently.boolean = True
    published_recently.short_description = "Published recently&"





