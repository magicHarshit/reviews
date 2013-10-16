from django.conf.urls.defaults import patterns, url
from django.contrib.auth.views import *

from .views import EndUserRegistration

urlpatterns = patterns('',
        url(r'^$', EndUserRegistration.as_view(), name='signup'),

        )