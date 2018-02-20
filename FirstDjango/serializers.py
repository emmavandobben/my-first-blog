from rest_framework import serializers

from blog.models import Post


#serializer converts model to json format
class PostSerializer(serializers.HyperlinkedIdentityField):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    text = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        return Post.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        return instance

    '''
    class Meta:
        model = Post
        fields = ('__all__')
    '''