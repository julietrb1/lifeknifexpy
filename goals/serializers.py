from rest_framework import serializers

from goals.models import Goal


class GoalSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Goal
        fields = ('url', 'question', 'test', 'frequency', 'cheat', 'style', 'startDate', 'owner')
