from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Topic(models.Model):
    """Topic created by a user."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Specific topic entry."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = RichTextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        return self.text[:50] + "..."


class Article(models.Model):
    """An article the user is writing about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class ArticleEntry(models.Model):
    """Specific entry for each article."""
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = RichTextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'articlesentries'

    def __str__(self):
        """Return a string representation of the model."""
        return self.text[:50] + "..."


class Comment(models.Model):
    """Comment crated by te user."""
    article = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
    user = models.CharField(max_length=255)
    comment_text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.comment_text)
