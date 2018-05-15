from django.conf.urls import url

from progress.views import *
from . import views

urlpatterns = [

    # Example: /
    url(r'^$', ProgressAlbumLV.as_view(), name='index'),

    # Example: /album/, same as /
    url(r'^album/$', ProgressAlbumLV.as_view(), name='album_list'),

    # Example: /album/99/
    url(r'^album/(?P<pk>\d+)/$', ProgressAlbumDV.as_view(), name='album_detail'),

    # Example: /photo/99/
    url(r'^photo/(?P<pk>\d+)/$', ProgressPhotoDV.as_view(), name='photo_detail'),

    # Example: /album/add/
    url(r'^album/add/$',
        ProgressAlbumPhotoCV.as_view(), name="album_add",
    ),

    # Example: /album/change/
    url(r'^album/change/$',
        ProgressAlbumChangeLV.as_view(), name="album_change",
    ),

    # Example: /album/99/update/
    url(r'^album/(?P<pk>[0-9]+)/update/$',
        ProgressAlbumPhotoUV.as_view(), name="album_update",
    ),

    # Example: /album/99/delete/
    url(r'^album/(?P<pk>[0-9]+)/delete/$',
        ProgressAlbumDeleteView.as_view(), name="album_delete",
    ),

    # Example: /photo/add/
    url(r'^photo/add/$',
        ProgressPhotoCreateView.as_view(), name="photo_add",
    ),

    # Example: /photo/change/
    url(r'^photo/change/$',
        ProgressPhotoChangeLV.as_view(), name="photo_change",
    ),

    # Example: /photo/99/update/
    url(r'^photo/(?P<pk>[0-9]+)/update/$',
        ProgressPhotoUpdateView.as_view(), name="photo_update",
    ),

    # Example: /photo/99/delete/
    url(r'^photo/(?P<pk>[0-9]+)/delete/$',
        ProgressPhotoDeleteView.as_view(), name="photo_delete",
    ),
]
