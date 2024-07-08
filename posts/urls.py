
from django.urls import path
from .views import PostViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', PostViewSet,basename='post')

urlpatterns = router.urls


# urlpatterns = [
#     path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
#     path("create/",PostCreate.as_view(),name='post_create'),
#     path('',PostList.as_view(),name='post_list'),
# ]