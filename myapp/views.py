from django.shortcuts import render
from myapp.models import Post, Author, Comment

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
    comments = Comment.objects.filter(post = post).all()
    context = {
        "post": post,
        "comments": comments,
    }
    return render(
        request,
        template_name="myapp/post_details.html",
        context=context,
    )

def get_posts_for_author(request, author_id):
    correct_author = Author.objects.get(id = author_id)
    posts_of_author = Post.objects.filter(author = correct_author).all()
    context = {
        "posts_of_author": posts_of_author,
        "author": correct_author
    }
    return render(
        request,
        template_name="myapp/author_posts.html",
        context=context
    )