from django.conf.urls import patterns, include, url
from django.contrib import admin

from views import ui

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scorekeeper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', ui.index),

    url(r'^match/(?P<match_id>\d+)/$', ui.match, name='view_match'),

    url(r'^admin/', include(admin.site.urls)),
)
