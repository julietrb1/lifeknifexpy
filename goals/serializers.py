from rest_framework import serializers

from common.serializers import OwnerSerializer
from goals.models import Goal, Answer


class GoalSerializer(OwnerSerializer):
    last_answered = serializers.DateField()

    class Meta:
        model = Goal
        fields = (
        'url', 'id', 'question', 'test', 'frequency', 'cheat', 'style', 'start_date', 'last_answered', 'owner')


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    def get_fields(self):
        fields = super().get_fields()
        fields['goal'].queryset = Goal.objects.filter(owner=self.context['request'].user)
        return fields

    class Meta:
        model = Answer
        fields = ('url', 'id', 'goal', 'value', 'date')
