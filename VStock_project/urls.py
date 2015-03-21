from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', logout_page),
    url(r'^portal/', include('VStock_app.urls')),
    url(r'^register/$', register, name='register'), # ADD NEW PATTERN!
)
