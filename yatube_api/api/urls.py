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
    r'v1/posts',
    PostsViewSet,
    basename='posts'
)
v1_router.register(
    r'v1/groups',
    GroupViewSet,
    basename='groups'
)
v1_router.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentsViewSet,
    basename='comments'
)
v1_router.register(
    r'v1/follow',
    FollowViewSet,
    basename='follow'
)

urlpatterns = [
    path('', include(v1_router.urls), name='api-root'),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
