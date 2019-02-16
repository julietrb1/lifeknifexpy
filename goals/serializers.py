from rest_framework import serializers

from common.serializers import OwnerSerializer
from goals.models import Goal, Answer


class GoalSerializer(OwnerSerializer):
    class Meta:
        model = Goal
        fields = ('url', 'id', 'question', 'test', 'frequency', 'cheat', 'style', 'start_date', 'owner')


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    def get_fields(self):
        fields = super().get_fields()
        fields['goal'].queryset = Goal.objects.filter(owner=self.context['request'].user)
        return fields

    class Meta:
        model = Answer
        fields = ('url', 'id', 'goal', 'value', 'date')
