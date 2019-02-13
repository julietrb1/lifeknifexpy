from common.views import UserViewSet
from goals.models import Goal
from goals.serializers import GoalSerializer


class GoalViewSet(UserViewSet):
    queryset = Goal.objects.all().order_by('question')
    serializer_class = GoalSerializer
