from django.conf.urls.defaults import patterns, url

from featured.views import FeaturedListView


urlpatterns = patterns('',
    url(r'^(?P<slug>[-\w]+)/(?P<model>(\w+\.\w+))/$', FeaturedListView.as_view(), name='featured_category_list'),
)
