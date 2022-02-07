from rest_framework import serializers
from blog.models import Blog
from account.models import User

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
