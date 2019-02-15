from common.views import UserViewSet
from nutrition.models import Food, Consumption
from nutrition.serializers import FoodSerializer, ConsumptionSerializer


class FoodViewSet(UserViewSet):
    queryset = Food.objects.all().order_by('name')
    serializer_class = FoodSerializer
    search_fields = ['name']
    filter_fields = ['is_archived']


class ConsumptionViewSet(UserViewSet):
    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer
