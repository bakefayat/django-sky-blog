from rest_framework import serializers
from web.models import Blog


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
