from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from login.views import *
from django.contrib.auth.decorators import login_required
from login import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangopool.views.home', name='home'),
    # url(r'^djangopool/', include('djangopool.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^$', login_page),
    # url(r'^login/$', Login_page.as_view()),
    # url(r'^$', 'django.contrib.auth.views.login'),
    # url(r'^logout/$', logout_page),
    # url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    # url(r'^register/$', register),
    # url(r'^register/success/$', register_success),
    # url(r'^home/$', home),

    # Uncomment the next line to enable the admin:
    # url(r'^$', include('accounts.urls', namespace="accounts")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    # url(r'^ui_statics/$', TemplateView.as_view(template_name="ui_statics/home.html"), name='ui_statics'),
    url(r'^ui_statics/$', TemplateView.as_view(template_name="ui_statics/index.html"), name='index'),
    # url(r'^ui_statics/$', TemplateView.as_view(template_name="index.html"), name='index')
    # Home Page
    # url(r'^$', login_required(views.IndexPageView.as_view()), name='index'),
)
