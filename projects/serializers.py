from rest_framework import serializers
from .models import Project, Tag


class TagSerializer(serializers.Serializer):
    name = serializers.SlugField(max_length=20)


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    tags = TagSerializer(many=True)

    class Meta:
        model = Project
        fields = ('url', 'id', 'name', 'description', 'source_link',
                  'website_link', 'author', 'author_link', 'creator',
                  'tags',)

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        project = Project.objects.create(**validated_data)
        # Save Tags
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(**tag_data)
            project.tags.add(tag)

        return project

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description',
                                                  instance.description)
        instance.source_link = validated_data.get('source_link',
                                                  instance.source_link)
        instance.website_link = validated_data.get('website_link',
                                                   instance.website_link)
        instance.author = validated_data.get('author', instance.author)
        instance.author_link = validated_data.get('author_link',
                                                  instance.author_link)

        # Remove old tags and Save new tags
        instance.tags.all().delete()
        tags_data = validated_data.get('tags', [])
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(**tag_data)
            instance.tags.add(tag)

        instance.save()
        return instance
