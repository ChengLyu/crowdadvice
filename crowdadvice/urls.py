from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^adviceapp/', include('adviceapp.urls', namespace="adviceapp")),
    url(r'^$', RedirectView.as_view(url='adviceapp/'))
)
