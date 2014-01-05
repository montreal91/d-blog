from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.BlogView.as_view(), name='index'),
    url(r'(?P<pk>\d+)/', views.PostView.as_view(), name='post'),
)