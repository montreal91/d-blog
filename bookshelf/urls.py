from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookshelf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('main.urls', namespace='main')),
    url(r'^shelf/', include('diary.urls', namespace='shelf')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^admin/', include(admin.site.urls)),
)
