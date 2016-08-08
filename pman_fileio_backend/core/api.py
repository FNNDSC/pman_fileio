from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns

from files import views

# API v1 endpoints
urlpatterns = format_suffix_patterns([

    url(r'^v1/fileupload/$', views.FileUploadList.as_view(), name='fileupload-list'),
    url(r'^v1/fileupload/(?P<pk>[0-9]+)/$', views.FileUploadDetail.as_view(), name='fileupload-detail'),
    url(r'^v1/fileupload/(?P<pk>[0-9]+)/.*$', views.FileResource.as_view(), name='file-resource'),

])

# Login and logout views for Djangos' browsable API
urlpatterns += [
    url(r'^v1/auth/', include('rest_framework.urls',  namespace='rest_framework')),
]

