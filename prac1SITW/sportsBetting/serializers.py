from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer

from models import *

class TeamSerializer (HyperlinkedModelSerializer):
    pass

class CompetitionSerializer (HyperlinkedModelSerializer):
    pass

class EventSerializer (HyperlinkedModelSerializer):
    pass

class BetSerializer (HyperlinkedModelSerializer):
    pass


