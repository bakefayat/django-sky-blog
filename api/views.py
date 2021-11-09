from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.generics import ListAPIView,ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
# from .serializers import ProductsSerializer, UserSerializer, CategorySerializer
from .permissions import IsSuperUser, IsStaffOrReadOnly, IsAuthorOrReadOnly, StaffReadOnlyOrSuperUser
# from web.models import Product, Category

# class ProductViewSet(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductsSerializer

#     def get_permissions(self):
#         if self.action in ['list', 'create']:
#             permission_classes = (IsStaffOrReadOnly,)
#         else:
#             permission_classes = (IsSuperUser,)
#         return [permission() for permission in permission_classes]
# # Create your views here.
# class ProductList(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductsSerializer
#     permission_classes = (IsStaffOrReadOnly,)


# class CategoryList(ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = (IsStaffOrReadOnly,)

# class ProductDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductsSerializer
#     lookup_field = 'pk'
#     permission_classes = (IsAuthorOrReadOnly, IsStaffOrReadOnly)

# class CategoryDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = (IsStaffOrReadOnly,)


# class UserList(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (StaffReadOnlyOrSuperUser, )