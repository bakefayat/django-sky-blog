from django.urls import path
from . import views
from .views import ArticleDetail, ArticleList, CategoryList
app_name = 'blog'
urlpatterns = [
    path('', ArticleList.as_view(), name='index'),
    path('page/<int:page>', ArticleList.as_view(), name='index'),
    path('single/<str:slug>', ArticleDetail.as_view(), name='single'),
    path('category/<str:slug>', CategoryList.as_view(), name='category'),
    path('category/<str:slug>/page/<int:page>', CategoryList.as_view(), name='category'),
]