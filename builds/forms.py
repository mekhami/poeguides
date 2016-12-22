from django import forms

from .models import Build


class BuildCreateForm(forms.ModelForm):
    class Meta:
        model = Build
        fields = ['description', 'patch', 'poeplanner_url', 'primary_skill', 'splash_image', 'tags', 'title']
