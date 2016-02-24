from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from worldcups import views

from worlcups.views import WorldcupViewSet, UserViewSet
from rest_framework import renderers

worldcup_list = WorldcupViewSet.as_view({
    'get' : 'list',
    'post' : 'create'
})

worldcup_detail = WorldcupViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'patch' : 'partial_update',
    'delete' : 'destroy'
})

user_list = UserViewSet.as_view({
    'get' : 'list'
})

user_detail = UserViewSet.as_view({
    'get' : 'retrieve'
})

urlpatterns = format_suffix_patterns([
    url(r'^worldcups/$', worldcup_list, name = 'worldcup_list'),
    url(r'^worldcups/(?P<pk>[0-9]+)/$', worldcup_detail, name = 'worldcup_detail'),
    url(r'^users/$', user_list, name = 'user_list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name = 'user_detail')
])

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),

]
