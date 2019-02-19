from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models

TEST_CHOICES = (('atleast', 'At least'), ('nomore', 'No more than'), ('never', 'Never'),)
STYLE_CHOICES = (('yesno', 'Yes/No'), ('likert', 'Likert'),)


class Goal(models.Model):
    question = models.CharField(max_length=100, validators=[MinLengthValidator(10)])
    test = models.CharField(choices=TEST_CHOICES, max_length=10)
    frequency = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)])
    cheat = models.PositiveSmallIntegerField(validators=[MinValueValidator(3), MaxValueValidator(14)], null=True,
                                             blank=True)
    style = models.CharField(choices=STYLE_CHOICES, max_length=10)
    start_date = models.DateField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def last_answered(self):
        latest_answer = self.answer_set.order_by('-date').first()
        return latest_answer.date if latest_answer else None

    def todays_answer_value(self):
        todays_answer = self.answer_set.filter(date=self.owner.lifeuser.get_current_time().date()).first()
        return todays_answer.value if todays_answer else None

    class Meta:
        unique_together = ('question', 'owner')

    def __str__(self):
        return self.question


class Answer(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
    date = models.DateField()

    class Meta:
        unique_together = ('goal', 'date')

    def __str__(self):
        return f'{self.date}: {self.goal.question}'
