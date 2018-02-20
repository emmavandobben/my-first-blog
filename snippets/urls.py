from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api/snippet/$', views.api_snippet_list, name='api_snippet_list'),
    url(r'^api/snippet/(?P<pk>[0-9]+)/$', views.api_snippet_detail, name='api_snippet_detail'),
]