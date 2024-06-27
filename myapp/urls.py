from django.urls import path
import myapp.views as ma_views

urlpatterns = [
    path("", ma_views.posts_list, name = "posts"),
    path("<int:post_id>/", ma_views.get_post_by_id, name = "post_details"),
    path("posts_authors/<int:author_id>/", ma_views.get_posts_for_author, name = "post_authors"),
]