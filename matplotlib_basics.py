# Matplotlib Basics - Creating Charts

import matplotlib.pyplot as plt

# Data
subjects = ["Math", "Science", "English", "Hindi", "Computer"]
marks = [85, 90, 78, 88, 95]

# Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(subjects, marks, color="green")
plt.title("Navin's Subject Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.savefig("marks_chart.png")
plt.show()

print("Chart saved!")

# Line Chart
months = ["Jan", "Feb", "Mar", "Apr", "May"]
progress = [60, 65, 72, 80, 90]

plt.figure(figsize=(8, 5))
plt.plot(months, progress, color="blue", marker="o")
plt.title("My Learning Progress")
plt.xlabel("Month")
plt.ylabel("Skills %")
plt.savefig("progress_chart.png")
plt.show()

print("Progress chart saved!")
