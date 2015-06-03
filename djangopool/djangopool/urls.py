from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangopool.views.home', name='home'),
    # url(r'^djangopool/', include('djangopool.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    # url(r'^ui_statics/$', TemplateView.as_view(template_name="ui_statics/home.html"), name='ui_statics'),
    url(r'^ui_statics/$', TemplateView.as_view(template_name="ui_statics/index.html"), name='index')
    # url(r'^ui_statics/$', TemplateView.as_view(template_name="index.html"), name='index')
    
)
