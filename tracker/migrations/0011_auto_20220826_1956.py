# Generated by Django 2.2 on 2022-08-26 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0010_auto_20220818_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='workout_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='workout',
            name='workout_time',
            field=models.TimeField(),
        ),
    ]