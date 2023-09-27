from blog.views import PostTagsViews, RetrieveDeletePost
from .views import PostList, PostListDetailfilter, CreatePost, EditPost
from django.urls import path

app_name = 'blog_api'

urlpatterns = [
    path('tag_post/slug=<slug>/', PostTagsViews, name="tag_post"),
    path('', PostList.as_view(), name='lists'),
    path('post/<str:pk>/', RetrieveDeletePost.as_view(), name='details'),
    path('search/', PostListDetailfilter.as_view(), name='searches'),
    path('create/', CreatePost.as_view(), name='creates'),
    path('edit/<int:pk>/', EditPost.as_view(), name='edits'),
]
