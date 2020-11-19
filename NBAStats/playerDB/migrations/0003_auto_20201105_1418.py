# Generated by Django 3.1.2 on 2020-11-05 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playerDB', '0002_auto_20201105_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='field_goals',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='player',
            name='field_goals_attempted',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='player',
            name='three_pts',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='player',
            name='three_pts_attempted',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='player',
            name='two_pts',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='player',
            name='two_pts_attempted',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]