from rest_framework import viewsets

from api.permissions import IsOwnerPermission
from api.serializers import CommentSerializer, GroupSerializer, PostSerializer
from api.utils import retrieve_post
from posts.models import Group, Post


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwnerPermission, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerPermission, )

    def get_queryset(self):
        post = retrieve_post(self)
        return post.comments

    def perform_create(self, serializer):
        post = retrieve_post(self)
        serializer.save(author=self.request.user, post=post)
