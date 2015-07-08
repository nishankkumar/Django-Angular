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

# urlpatterns = [
#     url(r'^profile/$', login_required(views.ProfileView.as_view()), name='profile'),
# ]


