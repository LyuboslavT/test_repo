my_workouts = []

def log_workout(workout, workout_type, duration):
    workout.append((workout_type, duration))

log_workout(my_workouts, 'run', 30)
log_workout(my_workouts, 'cycling', 30)
log_workout(my_workouts, 'yoga', 30)
log_workout(my_workouts, 'swiming', 30)

print(my_workouts)


