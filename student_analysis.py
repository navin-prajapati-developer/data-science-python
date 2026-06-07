# Student Data Analysis Project

import pandas as pd

# Student dataset
data = {
    "Name": ["Navin", "Rahul", "Priya", "Amit", "Sara"],
    "Math": [85, 90, 78, 92, 88],
    "Science": [80, 85, 90, 75, 92],
    "English": [75, 80, 85, 70, 95],
    "Computer": [95, 88, 82, 90, 85]
}

df = pd.DataFrame(data)

# Calculate total and average
df["Total"] = df["Math"] + df["Science"] + df["English"] + df["Computer"]
df["Average"] = df["Total"] / 4

# Assign grades
def get_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    else:
        return "C"

df["Grade"] = df["Average"].apply(get_grade)

print("--- Student Report ---")
print(df)
print("\nTop Student:", df.loc[df["Average"].idxmax(), "Name"])
print("Class Average:", df["Average"].mean())
