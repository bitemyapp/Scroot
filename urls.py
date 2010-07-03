from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
    (r'^log/(?P<object_id>\d+)/$', 'audit.views.log'),
)