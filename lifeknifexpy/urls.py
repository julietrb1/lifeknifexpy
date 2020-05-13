from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from goals.views import GoalViewSet, AnswerViewSet
from nutrition.views import ConsumptionViewSet, FoodViewSet
from sec.views import account

router = routers.DefaultRouter()
router.register('foods', FoodViewSet)
router.register('consumptions', ConsumptionViewSet)
router.register('goals', GoalViewSet)
router.register('answers', AnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('account/', account)
]
