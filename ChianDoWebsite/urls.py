from django.conf.urls import url, static
from thefuck.rules.fix_file import patterns

from ChianDo import settings
from . import views
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^b/(?P<pk>\d+)/$', views.BlogView.as_view(), name='post'),
    url(r'galerien',views.GalleryView.as_view(), name='galleries'),
    url(r'termine', views.EventView.as_view(), name='events'),
    url(r'archiv', views.ArchiveView.as_view(), name='archiv')
]