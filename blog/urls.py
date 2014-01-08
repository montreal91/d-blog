# -*- coding: utf-8 -*- 

from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.BlogView.as_view(), name='index'),
    url(r'^create/$', views.CreatePostView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/', views.UpdatePostView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/', views.DeletePostView.as_view(), name='delete'),
    url(r'(?P<pk>\d+)/', views.PostView.as_view(), name='post'),
)