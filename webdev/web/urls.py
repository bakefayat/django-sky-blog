from django.urls import path
from . import views
from .views import ArticleList, ArticleDetail, CategoryList, UserList
app_name = 'blog'
urlpatterns = [
    path('', ArticleList.as_view(), name='index'),
    path('page/<int:page>', ArticleList.as_view(), name='index'),
    path('<str:slug>', ArticleDetail.as_view(), name='single'),
    path('category/<str:slug>', CategoryList.as_view(), name='category'),
    path('category/<str:slug>/page/<int:page>', CategoryList.as_view(), name='category'),
    path('user/<str:slug>', UserList.as_view(), name='user'),
    path('user/<str:slug>/page/<int:page>', UserList.as_view(), name='user'),
]