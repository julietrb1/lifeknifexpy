from rest_framework import permissions, viewsets

from common.views import UserViewSet
from goals.models import Goal, Answer
from goals.serializers import GoalSerializer, AnswerSerializer


class GoalViewSet(UserViewSet):
    queryset = Goal.objects.all().order_by('question')
    serializer_class = GoalSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_fields = ['goal_id']

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(goal__owner=self.request.user).order_by('date')
        return query_set
