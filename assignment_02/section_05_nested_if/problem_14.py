# Check if number is positive/negative. If positive, check even/odd using nested if.
num = int(input("Enter a number: "))
if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
elif num < 0:
    print("Negative")
else:
    print("Zero")
