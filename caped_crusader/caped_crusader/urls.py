from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('caped_crusader.views',
    # Examples:
    # url(r'^$', 'caped_crusader.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^hello/', 'hello'),
    url(r'^addCollege/','addCollege'),
    url(r'^setCodechefDb/','setCodechefDb'),
    url(r'^updateCFUserlist/','updateCFUserlist'),
    url(r'^addCfUser/','addCfUser'),
    url(r'^addTCUser/','addTCUser'),
    url(r'^updateTCUserlist/','updateTCUserlist'),
    url(r'^setId/','setId'),
    url(r'^ccRankings/(?P<contest>\w+)/(?P<get_handle>\w+)', 'get_cc_rank'),
    url(r'^ccTable/(?P<contest>\w+)', 'ccTable'),
)
