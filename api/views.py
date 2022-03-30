from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ArticleSerializer, UserSerializer, CategorySerializer
from .permissions import IsSuperUserOrReadOnly, IsAuthorOrReadOnly, IsSuperUser
from blog.models import Blog, Category
from accounts.models import User


class ArticleListApiView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsSuperUserOrReadOnly,)


class ArticleDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "slug"
    permission_classes = (IsAuthorOrReadOnly,)


class UserListApiView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrReadOnly,)


class UserDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)


class CategoryListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsSuperUserOrReadOnly,)


class CategoryDetailAPIVIEW(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsSuperUserOrReadOnly,)
    lookup_field = "slug"


class RevokeTokenApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        request.auth.delete()
        return Response(status=204)
