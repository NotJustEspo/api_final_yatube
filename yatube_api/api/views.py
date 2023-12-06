from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets

from api.permissions import IsAuthorOrReadOnly
from api.serializers import CommentSerializer, GroupSerializer, PostSerializer, FollowSerializer
from posts.models import Group, Post, Follow, User


class PostsViewSet(viewsets.ModelViewSet):
    """
    Класс для работы с постами.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Класс для работы с группами.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    """
    Класс для работы с комментами.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def get_object_new(self):
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Post, pk=post_id)

    def get_queryset(self):
        return self.get_object_new().comments.all()

    def perform_create(self, serializer):
        post = self.get_object_new()
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    """
    Класс для работы с подписками.
    """
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated,]

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return user.follower.all()

    def perform_create(self, serializer):
        user = get_object_or_404(User, username=self.request.user)
        following = get_object_or_404(
            User,
            username=self.request.data.get('following')
        )
        serializer.save(user=user, following=following)
