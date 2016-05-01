from stores.views import store_list
from django.conf.urls import url,include
from . import views
from .views import store_list,store_detail
urlpatterns=[

    url(r'^new/$', views.store_create, name='store_create'),
    url(r'^$',views.store_list,name='store_list'),
    url(r'^(?P<pk>\d+)/$', views.store_detail, name='store_detail'),
    url(r'^(?P<pk>\d+)/update/$', views.store_update, name='store_update'),
]
