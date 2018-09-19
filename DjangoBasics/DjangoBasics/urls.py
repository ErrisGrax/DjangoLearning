"""
Definition of urls for DjangoBasics.
"""

from django.conf.urls import include, url
import HelloDjangoApp.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', DjangoBasics.views.home, name='home'),
    # url(r'^DjangoBasics/', include('DjangoBasics.DjangoBasics.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    #dodane wraz z HelloDjangoApp.views
    url(r'^$', HelloDjangoApp.views.index, name='index'),
    url(r'^home$', HelloDjangoApp.views.index, name='home'),
    url(r'^subpage1$', HelloDjangoApp.views.subpage1, name='subpage'),
    url(r'^timewatch$', HelloDjangoApp.views.timewatch, name='time'),
]
