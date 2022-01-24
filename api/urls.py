from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import ArticleListApiView, ArticleDetailApiView, UserListApiView, UserDetailApiView, RevokeTokenApiView
app_name = "api"

urlpatterns = [
    path("token/", obtain_auth_token, name="token"),
    path("revoke/", RevokeTokenApiView.as_view(), name="token"),
    path("", ArticleListApiView.as_view(), name="list"),
    path("detail/<str:slug>/", ArticleDetailApiView.as_view(), name="detail"),
    path("users/", UserListApiView.as_view(), name="user list"),
    path("users/<int:pk>", UserDetailApiView.as_view(), name="user list"),
]