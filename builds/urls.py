from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^create/$', views.BuildCreate.as_view(), name='create'),
    url(r'^delete/$', views.BuildDelete.as_view(), name='delete'),
    url(r'^(?P<slug>[\w-]+)/$', views.BuildDetail.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/publish$', views.publish_build, name='publish'),
]
