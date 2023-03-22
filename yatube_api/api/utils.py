from rest_framework.generics import get_object_or_404

from posts.models import Post


def retrieve_post(obj):
    post_id = obj.kwargs.get('post_id')
    return get_object_or_404(Post, id=post_id)
