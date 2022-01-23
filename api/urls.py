from django.urls import path
from .views import ArticleListApiView, ArticleDetailApiView
app_name = "api"

urlpatterns = [
    path("", ArticleListApiView.as_view(), name="list"),
    path("detail/<str:slug>", ArticleDetailApiView.as_view(), name="detail"),
]