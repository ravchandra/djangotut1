from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'polls'
'''
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
'''
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^accounts/login/$', auth_views.login, {'template_name':'polls/login.html'}, name='login'),
    url(r'^accounts/logout/$', views.logout_view, name='logout'),
    url(r'^upload_file/$', views.upload_file_view, name='upload_file'),
    url(r'^upload_success/$', views.upload_success_view, name='upload_success'),
    ]

