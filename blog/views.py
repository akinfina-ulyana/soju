from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.contrib.auth.models import User


# Create your views here.
class UserPostListView(ListView):
    model = Post
    context_object_name = 'blog_post_user_list'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_created')