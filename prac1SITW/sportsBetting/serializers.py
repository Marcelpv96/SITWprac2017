from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField, PrimaryKeyRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer

from models import *


class TeamSerializer (HyperlinkedModelSerializer):
    created_by = CharField(read_only=True)

    class Meta:
        model = Team
        fields = ('name', 'short_name', 'crest', 'created_by', )


class CompetitionSerializer (HyperlinkedModelSerializer):
    team_set = PrimaryKeyRelatedField(many=True, read_only=False, queryset=Team.objects.all(), source='teams')
    user = CharField(read_only=True)

    class Meta:
        model = Competition
        fields = ('name', 'short_name', 'logo', 'user', 'team_set')


class EventSerializer (HyperlinkedModelSerializer):
    user = CharField(read_only=True)
    sport = CharField(read_only=True)
    team1 = CharField(read_only=True)
    team2 = CharField(read_only=True)

    class Meta:
        model = Event
        fields = ('name', 'sport', 'user', 'team1', 'team2', )


class BetSerializer (HyperlinkedModelSerializer):
    user = CharField(read_only=True)
    event = CharField(read_only=True)

    class Meta:
        model = Bet
        fields = ('quota', 'description', 'user', 'event', )


