from pyexpat import model
from django import forms
from .models import Exercise, Workout

class CreateWorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        exclude = ['user']


class CreateExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        exclude = ['workout']
        labels = {
            'number_of_reps_per_set': 'Number of repetitions performed per set',
            'weight_per_rep': 'Weight per repetition in pounds',
            'workout': 'Existing workout to add exercise to'
             }
        widgets = {'workout': forms.Select(attrs={'class': 'workout-selector'})}

class EditExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        exclude = ['workout']
        labels = {
            'number_of_reps_per_set': 'Number of repetitions performed per set',
            'weight_per_rep': 'Weight per repetition in pounds',
            'workout': 'Existing workout to add exercise to'
             }
        widgets = {'workout': forms.Select(attrs={'class': 'workout-selector'})}