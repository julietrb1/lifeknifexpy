from rest_framework import serializers

from common.serializers import OwnerSerializer
from nutrition.models import Food, Consumption


class FoodSerializer(OwnerSerializer):
    class Meta:
        model = Food
        fields = ('id', 'url', 'name', 'health_index', 'is_archived', 'icon', 'owner')


class ConsumptionSerializer(OwnerSerializer):
    food_name = serializers.CharField(read_only=True)
    food_icon = serializers.CharField(read_only=True)

    def get_fields(self):
        fields = super().get_fields()
        fields['food'].queryset = Food.objects.filter(owner=self.context['request'].user)
        return fields

    class Meta:
        model = Consumption
        fields = ('id', 'url', 'food', 'date', 'quantity', 'owner', 'food_name', 'food_icon')
