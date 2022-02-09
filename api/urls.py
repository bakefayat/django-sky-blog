from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import ArticleListApiView, ArticleDetailApiView, UserListApiView, UserDetailApiView, RevokeTokenApiView, CategoryListAPIView, CategoryDetailAPIVIEW
app_name = "api"

urlpatterns = [
    path("token/", obtain_auth_token, name="token"),
    path("revoke/", RevokeTokenApiView.as_view(), name="token"),
    path("", ArticleListApiView.as_view(), name="list"),
    path("detail/<str:slug>/", ArticleDetailApiView.as_view(), name="detail"),
    path("categories/", CategoryListAPIView.as_view(), name="cat_list"),
    path("categories/detail/<str:slug>/", CategoryDetailAPIVIEW.as_view(), name="cat_detail"),
    path("users/", UserListApiView.as_view(), name="user_list"),
    path("users/<int:pk>", UserDetailApiView.as_view(), name="user_detail"),
]
