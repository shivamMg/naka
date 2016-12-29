from rest_framework import serializers
from .models import Project, Tag


class TagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class TagSerializer(serializers.Serializer):
    # Used in ProjectSerializer for custom tag creation
    name = serializers.SlugField(max_length=20)


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    sourceLink = serializers.URLField(source='source_link')
    websiteLink = serializers.URLField(source='website_link', allow_blank=True)
    authorLink = serializers.URLField(source='author_link', allow_blank=True)
    creator = serializers.ReadOnlyField(source='creator.username')
    tags = TagSerializer(many=True)

    class Meta:
        model = Project
        fields = ('url', 'id', 'name', 'description', 'sourceLink',
                  'websiteLink', 'author', 'authorLink', 'creator',
                  'tags', 'approved', 'created_at', )

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        # Save Project
        project = Project.objects.create(**validated_data)
        project.approved = False
        project.save()

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
        instance.approved = validated_data.get('approved',
                                               instance.approved)

        # Remove old tags and Save new tags
        instance.tags.all().delete()
        tags_data = validated_data.get('tags', [])
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(**tag_data)
            instance.tags.add(tag)

        instance.save()
        return instance
