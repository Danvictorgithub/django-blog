from django.http import JsonResponse
from django.urls import include, path


urlpatterns = [
    path("",lambda request: JsonResponse({"message":"Welcome to Django List"})),
    path('posts/',include('posts.urls')),
    path('users/',include('accounts.urls')),
    path('auth/',include('dj_rest_auth.urls')),
    path("auth/registration/",
         include("dj_rest_auth.registration.urls")),
]