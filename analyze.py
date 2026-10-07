import csv

INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

math_sum = 0
english_sum = 0
python_sum = 0
count = 0
best = ""
best_avg = 0
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    next(f)
    for line in f:
        line = line.strip()
        parts = line.split(",")
        name = parts[0]
        math = float(parts[1])
        python = float(parts[2])
        english = float(parts[3])
        math_sum += math
        english_sum += english
        python_sum += python
        count += 1
        student_avg = (math + english + python) / 3
        if student_avg > best_avg:
            best_avg = student_avg
            best = name

math_avg = math_sum / count
english_avg = english_sum / count
python_avg = python_sum / count

result = f"""Середній бал по класу:
math: {math_avg:.1f}
english: {english_avg:.1f}
python: {python_avg:.1f}

Найкращий студент: {best} ({best_avg:.1f})"""

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(result)

print(result)
