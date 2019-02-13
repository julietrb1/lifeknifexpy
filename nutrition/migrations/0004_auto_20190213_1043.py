# Generated by Django 2.1.7 on 2019-02-13 10:43

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nutrition', '0003_auto_20190213_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('quantity', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1),
                                                                          django.core.validators.MaxValueValidator(
                                                                              4)])),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='consumption',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutrition.Food'),
        ),
        migrations.AddField(
            model_name='consumption',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='consumption',
            unique_together={('date', 'owner', 'food')},
        ),
    ]