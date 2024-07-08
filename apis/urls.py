from django.http import JsonResponse
from django.urls import include, path


urlpatterns = [
    path("",lambda request: JsonResponse({"message":"Welcome to Django List"})),
     path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path('posts/',include('posts.urls')),
]