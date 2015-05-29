from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'submitpage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^myapp/', include('myapp.urls')),
    url(r'^.*$', RedirectView.as_view(url='myapp', permanent=False), name='index')
)
