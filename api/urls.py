from django.urls import path
from .views import ArticleListApiView, ArticleDetailApiView, UserListApiView, UserDetailApiView
app_name = "api"

urlpatterns = [
    path("", ArticleListApiView.as_view(), name="list"),
    path("detail/<str:slug>/", ArticleDetailApiView.as_view(), name="detail"),
    path("users/", UserListApiView.as_view(), name="user list"),
    path("users/<int:pk>", UserDetailApiView.as_view(), name="user list"),
]