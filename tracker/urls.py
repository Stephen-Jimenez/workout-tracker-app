from django.urls import path
from . import views

urlpatterns = [
    path('/home', views.index),
    path('/create_workout', views.create_workout),
    path('/create_exercise/<int:workout_id>', views.create_exercise),
    path('/view_previous_workouts', views.view_previous_workouts),
    path('/workout_detail/<int:id>', views.workout_detail),
    path('/delete_workout/<int:workout_id>', views.delete_workout),
    path('/delete_exercise/<int:exercise_id>', views.delete_exercise),
    path('/edit_exercise_display/<int:exercise_id>', views.edit_exercise_display),
    path('/edit_exercise/<int:exercise_id>', views.edit_exercise)
]