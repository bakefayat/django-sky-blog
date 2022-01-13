from django.urls import path
from .views import SimpleView
from .views import ArticleListApiView
app_name = "api"

urlpatterns = [
    path("", SimpleView.as_view(), name="home"),
    path("list/", ArticleListApiView.as_view(), name="List"),
]