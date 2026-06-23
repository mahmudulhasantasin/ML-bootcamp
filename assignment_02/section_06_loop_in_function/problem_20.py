# Function print_table(number) that prints multiplication table from 1 to 10.
def print_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

print_table(5)
