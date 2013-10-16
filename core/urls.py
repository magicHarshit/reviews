from django.conf.urls.defaults import patterns, url
from django.contrib.auth.views import *

from .views import EndUserRegistration, EndUserLogin

urlpatterns = patterns('',
        url(r'^$', EndUserRegistration.as_view(), name='signup'),

        url(r'^login/$', EndUserLogin.as_view(), name='signup'),

        )