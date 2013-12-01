from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^bootledger/$', 'boot_ledger.views.index'),
    # url(r'^bootledger/(?P<item_id>\d+)/$', 'boot_ledger.views.detail'),
    # url(r'^bootledger/(?P<item_id>\d+)/results/$', 'boot_ledger.views.results'),
    url(r'^admin/', include(admin.site.urls)),
)