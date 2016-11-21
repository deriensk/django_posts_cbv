from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static



from django.views.generic.base import TemplateView

from .views import (                    
                    PostDetail,
                    PostList,
                    PostCreate,
                    PostUpdate,
                    PostDelete,
                    )

urlpatterns = [
        
    url(r'^$', PostList.as_view(), name='post_list'),
    url(r'^create/$', PostCreate.as_view(), name='post_create'),
    url(r'^(?P<pk>\d+)/$', PostDetail.as_view(), name='post_detail'),
    
    url(r'^(?P<pk>\d+)/edit/$', PostUpdate.as_view(), name='post_update'),
    url(r'^(?P<pk>\d+)/delete/$', PostDelete.as_view(), name='post_delete'),
   
    
]

