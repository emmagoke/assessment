# Generated by Django 4.1 on 2023-08-10 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='season_best_for_crops',
            field=models.CharField(max_length=15),
        ),
    ]
