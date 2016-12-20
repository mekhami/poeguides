from django.shortcuts import render
from django.views import generic

from .forms import BuildCreateForm
from .models import Build


class IndexView(generic.ListView):
    template = 'builds/index.html'
    model = Build
    context_object_name = 'nonfeatured'

    def get_queryset(self):
        return Build.objects.filter(published=True, featured=False).order('-date_updated')

    def get_context_data(self):
        context = super().get_context_data()
        featured = Build.objects.filter(published=True, featured=True)
        context['featured'] = featured
        return context


class BuildDetail(generic.DetailView):
    model = Build


class BuildCreate(generic.FormView):
    model = Build
    form_class = BuildCreateForm


class BuildUpdate(generic.UpdateView):
    model = Build
    form_class = BuildCreateForm


class BuildDelete(generic.DeleteView):
    model = Build
    success_url = '/'


def publish_build(request):
    if not request.method == 'POST':
        raise Exception('How did you get here?')
    build = Build.objects.get(slug=request.kwargs['slug'])
    build.published = True
    build.save()
    return render(request, 'build/detail.html')
