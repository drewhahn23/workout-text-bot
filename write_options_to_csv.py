import json
import csv
import pandas as pd 

workouts = {
	'legs': {
	1: 'Front Squat',
	2: 'Back Squat',
	3: 'Deadlift',
	4: 'Russian Deadlift'
	},
	'arms': {
	1: 'Dumbell Curls',
	2: 'Barbell Curls',
	3: 'Cable Curls',
	4: 'Close-grip push-ups',
	5: 'Overhead Tricep Exentions',
	},
	'chest': {
	1: 'Barbell Bench',
	2: 'Dumbell Bench',
	3: 'Chest Press',
	4: 'Flies',
	5: 'Wide-grip push-ups'
	},
	'back': {
	1: 'Lat Pull-downs',
	2: 'Close-grip rows',
	3: 'Standing Dumbell rows',
	4: 'Wide-grip pull-ups',
	5: 'Standing Barbell rows'
	}
}

df = pd.DataFrame(workouts)

df.to_csv('workout_options.txt')