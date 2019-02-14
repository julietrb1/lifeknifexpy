from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=60)
    health_index = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
    is_archived = models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'owner')
        ordering = ('name',)


class Consumption(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    date = models.DateTimeField()
    quantity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.date.replace(minute=0, second=0, microsecond=0)
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f'{self.quantity}x {self.food.name}'

    class Meta:
        unique_together = ('date', 'owner', 'food')
        ordering = ('-date',)
