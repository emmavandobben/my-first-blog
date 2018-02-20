from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import Post


# serializer converts model to json format
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # The source arg is used to control which attribute populates a field
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'posts')
