from django.conf.urls import patterns, include, url

from django.contrib import admin
from django_apogee.views.django_apogee_views import anneuni_list

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_django_apogee.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^annesuni/$', anneuni_list),
    url(r'^admin/', include(admin.site.urls)),

)
