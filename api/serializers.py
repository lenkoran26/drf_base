from rest_framework import serializers


class GroupSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    slug = serializers.SlugField()
    description = serializers.CharField()