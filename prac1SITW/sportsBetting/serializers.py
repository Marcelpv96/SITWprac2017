from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer

from models import *


class TeamSerializer (HyperlinkedModelSerializer):
    created_by = CharField(read_only=True)
    uri = HyperlinkedIdentityField(view_name='team-detail')
    competitions = HyperlinkedRelatedField(many=True, read_only=True, view_name='competition-detail', source='competition_set')
    local_events = HyperlinkedRelatedField(many=True, read_only=True, view_name='event-detail', source='local')
    visitor_events = HyperlinkedRelatedField(many=True, read_only=True, view_name='event-detail', source='visitor')

    class Meta:
        model = Team
        fields = ('uri', 'name', 'short_name', 'crest', 'created_by', 'local_events', 'visitor_events', 'competitions')


class CompetitionSerializer (HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='competition-detail')
    team_set = TeamSerializer(many=True, source='teams')
    user = CharField(read_only=True)

    class Meta:
        model = Competition
        fields = ('uri', 'name', 'short_name', 'logo', 'user', 'team_set', )


class EventSerializer (HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='event-detail')
    user = CharField(read_only=True)
    team1 = TeamSerializer()
    team2 = TeamSerializer()

    class Meta:
        model = Event
        fields = ('uri', 'name', 'user', 'team1', 'team2',)


class BetSerializer (HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='bet-detail')
    user = CharField(read_only=True)
    event = EventSerializer()

    class Meta:
        model = Bet
        fields = ('uri', 'quota', 'description', 'user', 'event', )


