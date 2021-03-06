from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Flickr.views.home', name='home'),
    # url(r'^Flickr/', include('Flickr.foo.urls')),
    url (r'^tagSearch/(?P<tag>[\w|\W]+)/$', 'FlickrExtractor.views.search', name='search'),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^tag/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
