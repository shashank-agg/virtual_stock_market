from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    url(r'^$', views.portal_main_page),
    url(r'^(?P<symbol>[A-Z]+)/$', views.company_page),
    url(r'^account/$', views.account_view),
)
