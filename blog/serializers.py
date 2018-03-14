from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import Post


# serializer converts model to json format
class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        # The source arg is used to control which attribute populates a field
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ('__all__')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    lookup_field = 'pk'
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'posts')
