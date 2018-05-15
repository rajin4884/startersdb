from django.conf.urls import url

from plan.views import *
from . import views

urlpatterns = [

    # Example: /
    url(r'^$', PlanAlbumLV.as_view(), name='index'),

    # Example: /album/, same as /
    url(r'^album/$', PlanAlbumLV.as_view(), name='album_list'),

    # Example: /album/99/
    url(r'^album/(?P<pk>\d+)/$', PlanAlbumDV.as_view(), name='album_detail'),

    # Example: /photo/99/
    url(r'^photo/(?P<pk>\d+)/$', PlanPhotoDV.as_view(), name='photo_detail'),

    # Example: /album/add/
    url(r'^album/add/$',
        PlanAlbumPhotoCV.as_view(), name="album_add",
    ),

    # Example: /album/change/
    url(r'^album/change/$',
        PlanAlbumChangeLV.as_view(), name="album_change",
    ),

    # Example: /album/99/update/
    url(r'^album/(?P<pk>[0-9]+)/update/$',
        PlanAlbumPhotoUV.as_view(), name="album_update",
    ),

    # Example: /album/99/delete/
    url(r'^album/(?P<pk>[0-9]+)/delete/$',
        PlanAlbumDeleteView.as_view(), name="album_delete",
    ),

    # Example: /photo/add/
    url(r'^photo/add/$',
        PlanPhotoCreateView.as_view(), name="photo_add",
    ),

    # Example: /photo/change/
    url(r'^photo/change/$',
        PlanPhotoChangeLV.as_view(), name="photo_change",
    ),

    # Example: /photo/99/update/
    url(r'^photo/(?P<pk>[0-9]+)/update/$',
        PlanPhotoUpdateView.as_view(), name="photo_update",
    ),

    # Example: /photo/99/delete/
    url(r'^photo/(?P<pk>[0-9]+)/delete/$',
        PlanPhotoDeleteView.as_view(), name="photo_delete",
    ),
]
