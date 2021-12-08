from django.urls import path
from . import views
from .views import ArticleListView, ArticleDetailView, CategoryListView, UserListView

app_name = "blog"
urlpatterns = [
    path("", ArticleListView.as_view(), name="index"),
    path("page/<int:page>/", ArticleListView.as_view(), name="index"),
    path("<str:slug>/", ArticleDetailView.as_view(), name="single"),
    path("category/<str:slug>/", CategoryListView.as_view(), name="category"),
    path(
        "category/<str:slug>/page/<int:page>/", CategoryListView.as_view(), name="category"
    ),
    path("user/<str:slug>/", UserListView.as_view(), name="user"),
    path("user/<str:slug>/page/<int:page>/", UserListView.as_view(), name="user"),
]
