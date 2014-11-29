from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('caped_crusader.views',
    # Examples:
    # url(r'^$', 'caped_crusader.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^hello/', 'hello'),
    url(r'^checkCollege/', 'checkCollege'),
    url(r'^ccContestRanks/(?P<contest>\w+)', 'ccContestRanks'),
    url(r'^getCurrentContests/', 'getCurrentContests'),
    url(r'^getallColleges/', 'getallColleges'),
    url(r'^getCCContests/', 'getCCContests'),
    url(r'^getCCContestRank/(?P<contest>\w+)', 'getCCContestRank'),
    url(r'^addCollege/','addCollege'),
    url(r'^setCodechefDb/','setCodechefDb'),
    url(r'^updateCFUserlist/','updateCFUserlist'),
    url(r'^addCfUser/','addCfUser'),
    url(r'^addTCUser/','addTCUser'),
    url(r'^updateTCUserlist/','updateTCUserlist'),
    url(r'^setId/','setId'),
    url(r'^delId/','del_Id'),
    url(r'^ccRankings/(?P<contest>\w+)/(?P<get_handle>\w+)', 'get_cc_rank'),
    url(r'^ccTable/(?P<contest>\w+)', 'ccTable'),
    url(r'^fillCCTable/(?P<contest>\w+)', 'fillCCTable'),
    url(r'^fillCFTable/(?P<contest>\w+)', 'fillCFTable'),
    url(r'^updateCCRank/(?P<contest>\w+)/(?P<run>\d+)', 'updateCCcontestRank'),
    url(r'^updateCFRank/(?P<contest>\w+)/(?P<run>\d+)', 'updateCFcontestRank'),
    url(r'^addCCUser/', 'addCCUser'),
    url(r'^testCCauth/', 'testCCauth'),
    url(r'^updateCCNames/', 'updateCCNames'),
    url(r'^syncCCCollege/', 'syncCCCollege'),
    url(r'^updateSyncCFNames/', 'updateSyncCFNames'),
    url(r'^SyncTCColleges/', 'SyncTCColleges'),
    url(r'^updateCCRank/(?P<handle>\w+)', 'updateCCRank'),
    url(r'^updateCFRank/', 'updateCFRank'),
    url(r'^updateTCRank/', 'updateTCRank'),
    url(r'^cfTable/(?P<contest>\w+)', 'cfTable'),
    url(r'^correctCCCollegeId/', 'correctCCCollegeId'),
    url(r'^createProblemTableCF', 'createProblemTableCF'),
)

