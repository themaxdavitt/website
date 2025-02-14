#!/usr/bin/env -S uv run --script

# /// script
# dependencies = ["pandas"]
# ///

from collections import deque
import json
import sys

import pandas as pd
import numpy as np

KG_PER_LB = 0.453592

new_path = sys.argv[1]
old_path = sys.argv[2]

df = pd.read_csv(new_path, header=0)

# Only keep certain series
df = df[
    ["Date", "Exercise Name", "Set Order", "Weight", "Reps", "Notes", "Workout Notes"]
]


df.rename(
    columns={
        "Date": "date",
        "Exercise Name": "exercise",
        "Set Order": "set",
        "Weight": "weight_lb",
        "Reps": "reps",
        "Notes": "exercise_note",
        "Workout Notes": "workout_note",
    },
    inplace=True,
)

df = df.astype(
    {
        "date": "datetime64[s]",
        "exercise": "string",
        "set": "int64",
        "weight_lb": "int64",
        "reps": "int64",
        "exercise_note": "string",
        "workout_note": "string",
    }
)

workouts = df.groupby("date")
last_3_workouts = deque(workouts, 3)


def transform_exercises(exercise_name_exercises):
    exercise_name, exercises = exercise_name_exercises

    exercise_note = exercises["exercise_note"].replace({np.nan: None}).iloc[0]

    exercises.set_index("set", inplace=True)
    exercises = exercises.groupby(["weight_lb", "reps"]).size().reset_index(name="sets")
    exercises = exercises.round(0)

    # TODO: note that volume includes warmup for technical and not philosophical reasons
    exercises["volume"] = exercises["weight_lb"] * exercises["reps"] * exercises["sets"]
    total_volume = exercises["volume"].sum().item()

    # Brzycki formula for 1RM https://help.strongapp.io/article/133-1rm
    exercises["1rm"] = exercises["weight_lb"] * 36 / (37 - exercises["reps"])
    max_1rm = exercises["1rm"].max().round(0).astype(int).item()

    workload_str = ", ".join(
        f"{row.sets.astype(int).item()}x{row.reps.astype(int).item()} {row.weight_lb:.0f}lbs"
        for _, row in exercises.iterrows()
    )

    return {
        "name": exercise_name,
        "note": exercise_note,
        "workload": workload_str,
        "total_volume": total_volume,
        "max_1rm": max_1rm,
    }


def transform_workout(date_workout):
    date, workout = date_workout

    workout_note = workout["workout_note"].replace({np.nan: None}).iloc[0]

    return {
        "date": date.isoformat(),
        "note": workout_note,
        "exercises": list(map(transform_exercises, workout.groupby(["exercise"]))),
    }


with open("strong.json", "w") as f:
    json.dump(list(map(transform_workout, last_3_workouts)), f, indent=4)
