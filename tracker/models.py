from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Workout(models.Model):
    workout_date = models.DateField()
    workout_time = models.TimeField()
    user = models.ForeignKey(User, on_delete="models.CASCADE", null=True, blank=True)
    # exercise

    def __str__(self):
        return f"{self.workout_date} at {self.workout_time}"

class Exercise(models.Model):
    exercise_name = models.CharField(max_length=100)
    number_of_sets = models.IntegerField()
    number_of_reps_per_set = models.IntegerField()
    weight_per_rep = models.IntegerField()
    workout = models.ForeignKey(Workout, related_name="exercise", on_delete="models.CASCADE", null=True,)

    def __str__(self):
        return self.exercise_name
