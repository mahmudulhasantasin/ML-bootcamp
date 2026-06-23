n = int(input("Enter a number: "))
result = "Positive" if n > 0 else ("Negative" if n < 0 else "Zero")
print(result)
if n != 0:
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
