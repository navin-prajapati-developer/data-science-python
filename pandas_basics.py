# Pandas Basics - Working with Data

import pandas as pd

# Creating a simple dataset
data = {
    "Name": ["Navin", "Rahul", "Priya", "Amit"],
    "Age": [22, 25, 23, 24],
    "Score": [85, 90, 78, 92],
    "City": ["Mumbai", "Delhi", "Pune", "Chennai"]
}

# Create DataFrame
df = pd.DataFrame(data)

print("--- Student Data ---")
print(df)

print("\n--- Basic Info ---")
print("Total students:", len(df))
print("Average score:", df["Score"].mean())
print("Highest score:", df["Score"].max())
print("Lowest score:", df["Score"].min())

print("\n--- Top Scorer ---")
print(df[df["Score"] == df["Score"].max()])
