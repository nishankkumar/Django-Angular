from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

# urlpatterns = [
#     # ex: /polls/
#     url(r'^$', views.index, name='index'),
#     # ex: /polls/5/
#     # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#     url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#     # ex: /polls/5/vote/
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
# ]

urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    # url(r'^profile/$', login_required(views.ProfileView.as_view()), name='profile'),
    url(r'^(?P<pk>[0-9]+)/$', login_required(views.DetailView.as_view()), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', login_required(views.ResultsView.as_view()), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', login_required(views.vote), name='vote'),
    # url(
    #     r'^login/$',
    #     'django.contrib.auth.views.login',
    #     name='login',
    #     kwargs={'template_name': 'polls/login.html'}
    # ),
    # url(
    #     r'^logout/$',
    #     'django.contrib.auth.views.logout',
    #     name='logout',
    #     kwargs={'next_page': '/'}
    # ),
]
