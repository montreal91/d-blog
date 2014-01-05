# -*- coding: utf-8 -*- 

from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns ('',
	url(r'^$', views.index, name='index'),
	url(r'^contacts', views.contacts, name='contacts'),
)