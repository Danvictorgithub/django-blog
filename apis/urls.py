from django.http import JsonResponse
from django.urls import include, path


urlpatterns = [
    path("",lambda request: JsonResponse({"message":"Welcome to Django List"})),
    path('posts/',include('posts.urls')),
]