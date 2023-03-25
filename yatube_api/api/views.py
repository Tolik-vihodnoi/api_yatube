from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from api.permissions import IsOwnerPermission
from api.serializers import CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Group, Post


class GetPostMixin:

    @staticmethod
    def retrieve_post_obj(obj):
        post_id = obj.kwargs.get('post_id')
        return get_object_or_404(Post, id=post_id)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerPermission)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class CommentViewSet(GetPostMixin, viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsOwnerPermission)

    def get_queryset(self):
        post = self.retrieve_post_obj(self)
        return post.comments

    def perform_create(self, serializer):
        post = self.retrieve_post_obj(self)
        serializer.save(author=self.request.user, post=post)
