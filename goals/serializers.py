import pytz
from django.utils import timezone
from rest_framework import serializers

from common.serializers import OwnerSerializer
from goals.models import Goal, Answer


class GoalSerializer(OwnerSerializer):
    last_answered = serializers.DateField(read_only=True)

    class Meta:
        model = Goal
        fields = (
            'url', 'id', 'question', 'test', 'frequency', 'cheat', 'style', 'start_date', 'last_answered', 'owner')


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    date = serializers.DateField(read_only=True)

    def get_fields(self):
        fields = super().get_fields()
        fields['goal'].queryset = Goal.objects.filter(owner=self.context['request'].user)
        return fields

    def create(self, validated_data):
        validated_data['date'] = timezone.now().astimezone(
            pytz.timezone(self.context['request'].user.lifeuser.timezone)).date()
        return super().create(validated_data)

    class Meta:
        model = Answer
        fields = ('url', 'id', 'goal', 'value', 'date')
