from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.simple.direct_to_template', {
        'template': 'index.html'}, name='index'),

    # Legacy URL from Sphinx homepage
    url(r'home', 'django.views.generic.simple.redirect_to', {
        'url': '/'}, name='home'),

    url(r'^sentry/', include('sentry.web.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
