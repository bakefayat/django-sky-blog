from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ArticleSerializer, UserSerializer
from .permissions import IsSuperUserOrReadOnly, IsAuthorOrReadOnly, IsSuperUser
from blog.models import Blog
from accounts.models import User
# Create your views here.


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


class RevokeTokenApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        request.auth.delete()
        return Response(status=204)
