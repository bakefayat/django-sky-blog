from django.urls import path, include
# from .views import ProductList, ProductDetail, UserList, CategoryList, CategoryDetail
from . import views
urlpatterns = [
    # path('', ProductList.as_view(), name='home'),
    # path('<int:pk>', ProductDetail.as_view(), name='detail'),
    # path('user', UserList.as_view(), name='user'),
    # path('category', CategoryList.as_view(), name='category'),
    # path('category/<int:pk>', CategoryDetail.as_view(), name='CategoryDetail')
]
