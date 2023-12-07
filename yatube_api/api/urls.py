from django.urls import path, include
from django.conf.urls import url
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter
from rest_framework import permissions

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

schema_view = get_schema_view(
   openapi.Info(
      title="Yatube API",
      default_version='v1',
      description="Документация для приложения yatube проекта Yatube",
      contact=openapi.Contact(email="admin@yatube.ru"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
]
