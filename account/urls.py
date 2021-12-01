# The views used below are normally mapped in the AdminSite instance.
# This URLs file is used to provide a reliable view deployment for test purposes.
# It is also provided as a convenience to those who want to deploy these URLs
# elsewhere.

from django.contrib.auth import views
from django.urls import path
from .views import (
    Home,
    ArticleList,
    CreateArticle,
    UpdateArticle,
    DeleteArticle,
    PreviewArticle,
    UpdateProfile,
)
from django.views.generic import TemplateView

app_name = "account"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("articles/", ArticleList.as_view(), name="list"),
    path("articles/create/", CreateArticle.as_view(), name="create"),
    path("articles/upadte/<int:pk>/", UpdateArticle.as_view(), name="update"),
    path("articles/delete/<int:pk>/", DeleteArticle.as_view(), name="delete"),
    path("articles/preview/<str:slug>/", PreviewArticle.as_view(), name="preview"),
    path("profile/", UpdateProfile.as_view(), name="profile"),
]
