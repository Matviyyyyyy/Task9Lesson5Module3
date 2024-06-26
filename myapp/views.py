from django.shortcuts import render
from myapp.models import Post

# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(
        request,
        template_name="myapp/posts.html",
        context=context,
    )

def get_post_by_id(request, post_id):
    post = Post.objects.get(id = post_id)
    context = {
        "post": post,
    }
    return render(
        request,
        template_name="myapp/post_details.html",
        context=context,
    )