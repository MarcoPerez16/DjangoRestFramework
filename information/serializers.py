from rest_framework import serializers
from .models import Videogame

# AN importan part of Django Rest Framework is a serializer
# this defines the Api representation
# more infor at (https://www.django-rest-framework.org/api-guide/serializers/)
class VideogameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videogame
        fields = ('id', 'name', 'description', 'creation_date')
        read_only_fields = ('creation_date',)