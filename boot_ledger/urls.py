from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from boot_ledger.models import Item

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            template_name='boot_ledger/index.html')),