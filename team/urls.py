from django.conf.urls import url

from . import views
from team.views import *
# from design.views import *

# app_name = 'team'
urlpatterns = [
    url(r'^topic/$', views.topic, name='topic'),
    url(r'^member/$', views.member, name='member'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^plan/$', views.plan, name='plan'), # 블로그형태
    # url(r'^plan/detail/(?P<pk>\d+)/$', PlanPhotoDV.as_view(), name='planphoto_detail'),# 플로그 디테일
    # url(r'^plan/detail/photo/(?P<pk>\d+)/$', PlanDV.as_view(), name='plan_detail'), # 완전 속시
    url(r'^sitemap/$', views.sitemap, name='sitemap'),
    # url(r'^design/$', in.design, name='design'),

]
