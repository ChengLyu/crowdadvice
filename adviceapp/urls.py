from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from adviceapp.views import mentee 

urlpatterns = patterns('',
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {'template_name' : 'adviceapp/login.html'},
        name='login'),
    url(r'^mentee/plan/$', mentee.plan, name='menteeplan'),
    url(r'^mentee/$',
        RedirectView.as_view(url=reverse_lazy('adviceapp:menteeplan')),
        name='mentee'),
    url(r'^$',
        RedirectView.as_view(url=reverse_lazy('adviceapp:menteeplan')),
        name='main')
)