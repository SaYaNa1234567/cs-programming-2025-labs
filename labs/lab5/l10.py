students = [("Анна", [5, 4, 5]), ("Иван", [3, 4, 4]), ("Мария", [5, 5, 5])]

student_grades = {}
for name, grades in students:
    student_grades[name] = sum(grades) / len(grades)

best_student = max(student_grades, key=student_grades.get)
best_grade = student_grades[best_student]

print(f"\n{best_student} имеет наивысший средний балл: {best_grade:.1f}")
