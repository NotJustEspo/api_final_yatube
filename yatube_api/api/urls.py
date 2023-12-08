from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import (
    PostsViewSet,
    GroupViewSet,
    CommentsViewSet,
    FollowViewSet
)


v1_router = DefaultRouter()
v1_router.register(
    'posts',
    PostsViewSet,
    basename='posts'
)
v1_router.register(
    'groups',
    GroupViewSet,
    basename='groups'
)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentsViewSet,
    basename='comments'
)
v1_router.register(
    'follow',
    FollowViewSet,
    basename='follow'
)

urlpatterns = [
    path('v1/', include(v1_router.urls), name='api-root'),
    path('v1/', include('djoser.urls.jwt')),
]
