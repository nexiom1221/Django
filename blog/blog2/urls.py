from django.urls import path,re_path
from blog2 import views

app_name = 'blog2'

urlpatterns = [
    # /blog2/
    path('', views.PostLV.as_view(), name='index'),

    # /blog2/post
    path('post/', views.PostLV.as_view(), name='post_list'),

    # /blog2/post/django-exsample
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),

    # /blog2/archive
    path('archive/', views.PostAV.as_view(), name='post_archive'),

    # /blog2/archive/2021
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),

    # /blog2/archive/2021/aug
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'),

    # /blog2/archive/2021/aug/09
    path('archive/<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),

    # /blog2/archive/today
    path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'),

    # /blog2/tag
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),

    # /blog2/tag/tagname
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),

]