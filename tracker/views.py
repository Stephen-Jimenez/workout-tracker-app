from django.shortcuts import render, redirect
from .forms import CreateExerciseForm, CreateWorkoutForm, EditExerciseForm
from django.contrib.auth.models import User
from .models import Workout, Exercise
from datetime import datetime

def index(request):
    workout_form = CreateWorkoutForm(initial = {'workout_date': datetime.now(), 'workout_time': datetime.now().time()})
    context = {
        'workout_form': workout_form,
    }
    return render(request, 'home.html', context)

def create_workout(request):
    if request.POST:
        form = CreateWorkoutForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
    return redirect(f"/tracker/workout_detail/{obj.id}")

def create_exercise(request, workout_id):
    if request.POST :
        form = CreateExerciseForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.workout = Workout.objects.get(id = workout_id)
            obj.save()
    return redirect(f"/tracker/workout_detail/{workout_id}")

def view_previous_workouts(request):
    current_user = request.user
    context = {
        'current_user_workouts': Workout.objects.filter(user = current_user).order_by('-id')
    }
    return render(request, "view_previous_workouts.html", context)

def workout_detail(request, id):
    exercise_form = CreateExerciseForm()
    current_workout = Workout.objects.get(id = id)
    context = {
        'current_workout': current_workout,
        'current_workout_exercises': current_workout.exercise.all().order_by('-id'),
        'exercise_form': exercise_form
    }
    return render(request, 'workout_detail.html', context)

def delete_workout(request, workout_id):
    workout_to_delete = Workout.objects.get(id = workout_id)
    workout_to_delete.delete()
    return redirect("/tracker/view_previous_workouts")

def delete_exercise(request, exercise_id):
    exercise_to_delete = Exercise.objects.get(id = exercise_id)
    workout_exercise_belongs_to = exercise_to_delete.workout
    exercise_to_delete.delete()
    return redirect(f"/tracker/workout_detail/{workout_exercise_belongs_to.id}")

def edit_exercise_display(request, exercise_id):
    current_exercise =  Exercise.objects.get(id = exercise_id)
    exercise_form = EditExerciseForm(initial={'exercise_name': current_exercise.exercise_name, 'number_of_sets': current_exercise.number_of_sets, 'number_of_reps_per_set': current_exercise.number_of_reps_per_set, 'weight_per_rep': current_exercise.weight_per_rep})
    context = {
        'current_exercise': current_exercise,
        'current_workout': current_exercise.workout,
        'exercise_form': exercise_form
    }
    return render(request, "edit_exercise.html", context)

def edit_exercise(request, exercise_id):
    current_exercise = Exercise.objects.get(id = exercise_id)
    current_workout = current_exercise.workout
    if request.POST:
        form = CreateExerciseForm(request.POST, instance=current_exercise)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.workout = current_workout
            obj.save()
    return redirect(f"/tracker/workout_detail/{current_workout.id}")