from rest_framework import serializers
from worlcups.models import Worldcup
from django.contrib.auth.models import User

class WorldcupSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')

    class Meta:
        model = Worldcup
        fields = ('url', 'owner', 'title', 'description', 'year', 'winner', 'runner_up')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    worldcups = serializers.HyperlinkedRelatedField(many = True, view_name = 'worlcup-detail', read_only = True)

    class Meta:
        model = User
        fields = ('id', 'username', 'worldcups')
