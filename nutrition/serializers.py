from rest_framework import serializers

from nutrition.models import Food, Consumption


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Food
        fields = ('url', 'name', 'health_index', 'is_archived', 'owner')


class ConsumptionSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    def get_fields(self):
        fields = super().get_fields()
        fields['food'].queryset = Food.objects.filter(owner=self.context['request'].user)
        return fields

    class Meta:
        model = Consumption
        fields = ('url', 'food', 'date', 'quantity', 'owner')
