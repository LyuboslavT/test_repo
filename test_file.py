# my_workouts = []
#
# def log_workout(workout, workout_type, duration):
#     workout.append((workout_type, duration))
#
# log_workout(my_workouts, 'run', 30)
# log_workout(my_workouts, 'cycling', 30)
# log_workout(my_workouts, 'yoga', 30)
# log_workout(my_workouts, 'swiming', 30)
#
#
#
# print(my_workouts)

# workouts = [5, 4, 3, 2, 2]
#
# time = sum(duration for duration in workouts)
#
# print(time)

import tkinter as tk
from tkinter import messagebox

# Data storage
workouts = []
calories = []


# Function to log workouts
def log_workout():
    workout_type = workout_entry.get()
    try:
        duration = int(duration_entry.get())
        workouts.append((workout_type, duration))
        workout_listbox.insert(tk.END, f"{workout_type} - {duration} min")
        messagebox.showinfo("Success", "Workout logged!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for duration.")


# Function to log calorie intake
def log_calories():
    try:
        calories_consumed = int(calories_entry.get())
        calories.append(calories_consumed)
        messagebox.showinfo("Success", "Calorie intake logged!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for calories.")


# Function to view progress
def view_progress():
    total_time = sum(duration for _, duration in workouts)
    total_calories = sum(calories)

    progress_text = f"Total Workout Time: {total_time} min\nTotal Calories: {total_calories}"

    if total_time <= 30:
        progress_text += "\nKeep going! You need more activity."
    elif total_time <= 60:
        progress_text += "\nGreat job! Keep up the progress."
    else:
        progress_text += "\nAmazing effort! You're on fire!"

    messagebox.showinfo("Progress", progress_text)


# Create GUI Window
root = tk.Tk()
root.title("Fitness Tracker")

# Workout input fields
tk.Label(root, text="Workout Type:").grid(row=0, column=0)
workout_entry = tk.Entry(root)
workout_entry.grid(row=0, column=1)

tk.Label(root, text="Duration (min):").grid(row=1, column=0)
duration_entry = tk.Entry(root)
duration_entry.grid(row=1, column=1)

tk.Button(root, text="Log Workout", command=log_workout).grid(row=2, column=0, columnspan=2)

# Calorie input field
tk.Label(root, text="Calories Consumed:").grid(row=3, column=0)
calories_entry = tk.Entry(root)
calories_entry.grid(row=3, column=1)

tk.Button(root, text="Log Calories", command=log_calories).grid(row=4, column=0, columnspan=2)

# Listbox to display workouts
tk.Label(root, text="Workout History:").grid(row=5, column=0)
workout_listbox = tk.Listbox(root, height=5, width=30)
workout_listbox.grid(row=6, column=0, columnspan=2)

# View progress button
tk.Button(root, text="View Progress", command=view_progress).grid(row=7, column=0, columnspan=2)

# Run the Tkinter event loop
root.mainloop()
