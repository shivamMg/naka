from django.db import models

from users.models import User


class Tag(models.Model):
    """Framework and Language tag for Projects.
    """
    name = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    source_link = models.URLField()
    website_link = models.URLField(blank=True)
    approved = models.BooleanField(default=False)

    tags = models.ManyToManyField(Tag)

    author = models.CharField(max_length=30)
    author_link = models.URLField(blank=True)

    creator = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
