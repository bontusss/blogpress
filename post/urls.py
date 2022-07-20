from django.urls import path

from post.views import post_detail, postListView, post_list, index


app_name = 'post'

urlpatterns = [
    path('', index, name='index'),
    # path('', postListView.as_view(), name='post-list'),
    path('posts', post_list, name="post-list"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post-detail'),
    path('tag/<slug:tag_slug>/', post_list, name='post_list_by_tag')
]
