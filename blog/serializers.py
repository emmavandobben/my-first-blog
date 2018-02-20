from rest_framework import serializers

from blog.models import Post


# serializer converts model to json format
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('__all__')
