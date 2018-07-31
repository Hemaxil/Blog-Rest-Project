from django.contrib import admin
from django.conf.urls import url
from .views import *

#always put app_name
app_name='Blog'
urlpatterns = [
    url(r'^$',PostListAPIView.as_view(),name="lists"),
    url(r'^create',PostCreateAPIView.as_view(),name='create'),
    url(r'^(?P<slug>[\w-]+)/update',PostUpdateAPIView.as_view(),name="update"),
    url(r'^(?P<slug>[\w-]+)/delete',PostDeleteAPIView.as_view(),name='delete'),
    url(r'(?P<slug>[\w-]+)',PostDetailAPIView.as_view(),name="details"),
]
# defining path for static files to be stored
