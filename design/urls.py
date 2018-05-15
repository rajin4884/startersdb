from django.conf.urls import url

from design.views import *
from . import views

urlpatterns = [

    # Example: /
    url(r'^$', DesignAlbumLV.as_view(), name='index'),

    # Example: /album/, same as /
    url(r'^album/$', DesignAlbumLV.as_view(), name='album_list'),

    # Example: /album/99/
    url(r'^album/(?P<pk>\d+)/$', DesignAlbumDV.as_view(), name='album_detail'),

    # Example: /photo/99/
    url(r'^photo/(?P<pk>\d+)/$', DesignPhotoDV.as_view(), name='photo_detail'),

    # Example: /album/add/
    url(r'^album/add/$',
        DesignAlbumPhotoCV.as_view(), name="album_add",
    ),

    # Example: /album/change/
    url(r'^album/change/$',
        DesignAlbumChangeLV.as_view(), name="album_change",
    ),

    # Example: /album/99/update/
    url(r'^album/(?P<pk>[0-9]+)/update/$',
        DesignAlbumPhotoUV.as_view(), name="album_update",
    ),

    # Example: /album/99/delete/
    url(r'^album/(?P<pk>[0-9]+)/delete/$',
        DesignAlbumDeleteView.as_view(), name="album_delete",
    ),

    # Example: /photo/add/
    url(r'^photo/add/$',
        DesignPhotoCreateView.as_view(), name="photo_add",
    ),

    # Example: /photo/change/
    url(r'^photo/change/$',
        DesignPhotoChangeLV.as_view(), name="photo_change",
    ),

    # Example: /photo/99/update/
    url(r'^photo/(?P<pk>[0-9]+)/update/$',
        DesignPhotoUpdateView.as_view(), name="photo_update",
    ),

    # Example: /photo/99/delete/
    url(r'^photo/(?P<pk>[0-9]+)/delete/$',
        DesignPhotoDeleteView.as_view(), name="photo_delete",
    ),
]
