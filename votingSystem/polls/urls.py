# coding=utf8
# author=lishengshen
from django.urls import path, re_path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    re_path('detail/(?P<pk>[0-9]+)', views.DetailView.as_view(), name='detail'),
    re_path('vote/(?P<question_id>[0-9]+)', views.vote, name='vote'),
    re_path('results/(?P<pk>[0-9]+)', views.ResultsView.as_view(), name='results'),
]
