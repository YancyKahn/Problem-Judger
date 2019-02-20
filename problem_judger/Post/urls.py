from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include
from Post import views
appname = 'Post'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<category_name>[a-zA-Z0-9_\u4e00-\u9fa5]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<category_name>[a-zA-Z0-9_\u4e00-\u9fa5]+)/results/$', views.results, name='results'),
    # path(r'', include ('Post.urls', mamespace="Post")),
]