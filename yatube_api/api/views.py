from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.pagination import LimitOffsetPagination

from .permissions import IsAuthorOrReadOnly
from .serializers import (
    GroupSerializer,
    PostSerializer,
    CommentSerializer,
    FollowSerializer
)
from posts.models import Group, Post
from rest_framework import filters


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthorOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly
    ]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthorOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get("id"))

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self.get_post()
        )

    def get_queryset(self):
        return self.get_post().comments


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.follower.all()
