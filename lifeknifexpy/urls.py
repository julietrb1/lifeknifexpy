from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from goals.views import GoalViewSet
from nutrition.views import ConsumptionViewSet, FoodViewSet

router = routers.DefaultRouter()
router.register(r'foods', FoodViewSet)
router.register(r'consumptions', ConsumptionViewSet)
router.register(r'goals', GoalViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
