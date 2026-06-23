# Take marks, check pass/fail. If passed, use nested if for grade (A, B, C).
marks = int(input("Enter marks: "))
if marks >= 40:
    if marks >= 80:
        print("Pass - A")
    elif marks >= 60:
        print("Pass - B")
    else:
        print("Pass - C")
else:
    print("Fail")
