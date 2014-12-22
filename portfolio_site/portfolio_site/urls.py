from django.conf.urls import patterns, include, url
from django.contrib import admin

from blog import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portfolio_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^portfolio/$', views.portfolio, name='portfolio'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^admin/', include(admin.site.urls)),
)
