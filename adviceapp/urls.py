from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from adviceapp.views import feed 

urlpatterns = patterns('',
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {'template_name' : 'adviceapp/login.html'},
        name='login'),
    url(r'^feed/$', feed.handle, name='feed'),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('adviceapp:feed')))
)