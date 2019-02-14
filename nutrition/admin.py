from django.contrib import admin

from nutrition.models import Food, Consumption

admin.site.register(Food)


class ConsumptionAdmin(admin.ModelAdmin):
    list_display = ('date', 'food', 'quantity', 'owner')


admin.site.register(Consumption, ConsumptionAdmin)
