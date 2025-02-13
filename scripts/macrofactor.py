#!/usr/bin/env -S uv run --script

# /// script
# dependencies = ["pandas[excel]"]
# ///

import sys

import pandas as pd

KG_PER_LB = 0.453592

new_path = sys.argv[1]
old_path = sys.argv[2]

calories_and_macros = pd.read_excel(
    new_path, sheet_name="Calories & Macros", index_col=0
)
scale_weight = pd.read_excel(new_path, sheet_name="Scale Weight", index_col=0)
weight_trend = pd.read_excel(new_path, sheet_name="Weight Trend", index_col=0)
expenditure = pd.read_excel(new_path, sheet_name="Expenditure", index_col=0)

# Merge on date
new_df = pd.concat(
    [calories_and_macros, scale_weight, weight_trend, expenditure], axis=1
)

# Only keep certain series
new_df = new_df[
    [
        "Calories (kcal)",
        "Protein (g)",
        "Fat (g)",
        "Carbs (g)",
        "Weight (lbs)",
        "Trend Weight (lbs)",
        "Expenditure",
    ]
]

# Rename stuff
new_df.rename(
    columns={
        "Calories (kcal)": "in_kcal",
        "Protein (g)": "protein_g",
        "Fat (g)": "fat_g",
        "Carbs (g)": "carb_g",
        "Weight (lbs)": "scale_weight_lb",
        "Trend Weight (lbs)": "trend_weight_lb",
        "Expenditure": "out_kcal",
    },
    inplace=True,
)
new_df.index.names = ["date"]

# Add computed series
new_df["scale_weight_kg"] = (new_df.scale_weight_lb * KG_PER_LB).round(2)
new_df["trend_weight_kg"] = (new_df.trend_weight_lb * KG_PER_LB).round(2)
new_df["deficit_kcal"] = new_df.out_kcal - new_df.in_kcal

# Merge new data into old
try:
    old_df = pd.read_json(old_path, orient="table")
    old_df = pd.concat([old_df, new_df]).drop_duplicates().sort_index()
except:
    old_df = new_df

print(old_df)
old_df.to_json(old_path, orient="table")
