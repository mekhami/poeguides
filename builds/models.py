from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from taggit.managers import TaggableManager
from django.utils.text import slugify


class Build(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    blurb = models.ForeignKey('BuildBlurb', null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    description = models.TextField(null=True, blank=True)
    featured = models.BooleanField(default=False)
    patch = models.DecimalField(decimal_places=1, max_digits=5)
    poeplanner_url = models.URLField(null=True, blank=True)
    primary_skill = models.CharField(max_length=100, null=True, blank=True)
    published = models.BooleanField(default=False)
    slug = models.CharField(max_length=255, null=True, blank=True)
    splash_image = models.ImageField(null=True, blank=True)
    tags = TaggableManager()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.author + ' ' + self.title

    def save(self):
        super().save()
        if not self.pk:
            self.slug = slugify(self.title)
            super().save()

    def get_absolute_url(self):
        return reverse('builds:detail', kwargs={'slug': self.slug})


class BuildBlurb(models.Model):
    content = models.TextField()
    order = models.IntegerField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class BuildBookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    build = models.ForeignKey('Build')

    def __str__(self):
        return self.user + ' ' + self.build.title


class BuildVideo(models.Model):
    url = models.URLField()
    build = models.ForeignKey('Build')

    def __str__(self):
        return self.build.title + ' ' + self.url
