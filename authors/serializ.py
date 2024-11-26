from rest_framework import serializers

from authors.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    class Meta:
        model = Author
        fields = '__all__'
