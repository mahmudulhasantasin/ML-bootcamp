# Take score 0-100, print grade (A+, A, B, C, F) and Pass/Fail.
score = int(input("Enter score (0-100): "))
if score >= 90:
    grade = "A+"
elif score >= 80:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >= 40:
    grade = "C"
else:
    grade = "F"
print(f"Grade: {grade}")
print("Pass" if score >= 40 else "Fail")
