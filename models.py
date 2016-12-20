from django import models
from django.conf import settings
from django.shortcuts import reverse
from django.taggit import TaggitManager
from django.template.filters import slugify

from . import constants


class Build(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    blurb = models.ForeignKey('BuildBlurb', null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    description = models.TextField(null=True, blank=True)
    featured = models.BooleanField(default=False)
    patch = models.DecimalField(places=1)
    poeplanner_url = models.URLField(null=True, blank=True)
    primary_skill = models.CharField(choices=constants.SKILL_CHOICES)
    published = models.BooleanField(default=False)
    slug = models.CharField(max_length=255, null=True, blank=True)
    splash_image = models.ImageField(null=True, blank=True)
    tags = TaggitManager(null=True, blank=True)
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
