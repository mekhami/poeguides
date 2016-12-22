from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from .forms import BuildCreateForm
from .models import Build


class IndexView(generic.ListView):
    template_name = 'pages/home.html'
    model = Build
    context_object_name = 'nonfeatured'

    def get_queryset(self):
        return Build.objects.filter(published=True, featured=False).order_by('-date_updated')

    def get_context_data(self):
        context = super().get_context_data()
        featured = Build.objects.filter(published=True, featured=True)
        context['featured'] = featured
        return context


class BuildDetail(generic.DetailView):
    model = Build


class BuildCreate(generic.FormView):
    template_name = 'builds/create.html'
    model = Build
    form_class = BuildCreateForm

    def form_valid(self, form):
        form.author = self.request.user
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return self.object.get_absolute_url()


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
