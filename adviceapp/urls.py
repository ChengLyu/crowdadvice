from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from adviceapp.views import (signup_mentee, signup_mentor, mentee, updatescore,
                             landing, )

urlpatterns = patterns('',
    url(r'^landing/$', landing.landing, name='landing'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {'template_name' : 'adviceapp/login.html'},
        name='login'),
    url(r'^logout/$',
        'django.contrib.auth.views.logout',
        {'next_page' : reverse_lazy('adviceapp:landing')},
        name='logout'),
    url(r'^mentee/createprofile/$',
        mentee.create_profile,
        name='menteecreateprofile'),
    url(r'^mentee/signup/$', signup_mentee.signup, name='menteesignup'),
    url(r'^mentee/plan/$', mentee.plan, name='menteeplan'),
    url(r'^mentor/signup/$', signup_mentor.signup, name='mentorsignup'),
    url(r'^update/all/$', updatescore.update_all, name='updateall'),
    url(r'^mentee/$',
        RedirectView.as_view(url=reverse_lazy('adviceapp:menteeplan')),
        name='mentee'),
    url(r'^$',
        RedirectView.as_view(url=reverse_lazy('adviceapp:landing')),
        name='main')
)