# The views used below are normally mapped in the AdminSite instance.
# This URLs file is used to provide a reliable view deployment for test purposes.
# It is also provided as a convenience to those who want to deploy these URLs
# elsewhere.

from django.contrib.auth import views
from django.urls import path
from .views import (
    HomeView,
    ArticleListView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticlePreviewView,
    ProfileUpdateView,
    ArticleDetailView,
    CategoryListView,
    CategoryCreateView,
    CategoryDetailView,
    CategoryUpdateView, CategoryDeleteView, CommentListView, CommentUpdateView, CommentDeleteView, CommentAcceptView,
    LogEventsListView,
)

app_name = "accounts"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),

    path("articles/", ArticleListView.as_view(), name="list"),
    path("articles/create/", ArticleCreateView.as_view(), name="create"),
    path("articles/update/<int:pk>/", ArticleUpdateView.as_view(), name="update"),
    path("articles/delete/<int:pk>/", ArticleDeleteView.as_view(), name="delete"),
    path("articles/preview/<str:slug>/", ArticlePreviewView.as_view(), name="preview"),
    path("articles/detail/<str:slug>/", ArticleDetailView.as_view(), name="detail"),

    path("categories/", CategoryListView.as_view(), name="cat_list"),
    path("categories/create/", CategoryCreateView.as_view(), name="cat_create"),
    path("categories/detail/<str:slug>/", CategoryDetailView.as_view(), name="cat_detail"),
    path("categories/update/<int:pk>/", CategoryUpdateView.as_view(), name="cat_update"),
    path("categories/delete/<int:pk>/", CategoryDeleteView.as_view(), name="cat_delete"),

    path("comments/", CommentListView.as_view(), name="comment_list"),
    path("comments/update/<int:pk>/", CommentUpdateView.as_view(), name="comment_update"),
    path("comments/delete/<int:pk>/", CommentDeleteView.as_view(), name="comment_delete"),
    path("comments/accept/<int:pk>/", CommentAcceptView.as_view(), name="comment_accept"),

    path("profile/", ProfileUpdateView.as_view(), name="profile"),

    path("log/", LogEventsListView.as_view(), name="log")
]
