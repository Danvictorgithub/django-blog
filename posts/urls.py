
from django.urls import path
from .views import PostDetail, PostList,PostCreate

urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("create/",PostCreate.as_view(),name='post_create'),
    path('',PostList.as_view(),name='post_list'),
]