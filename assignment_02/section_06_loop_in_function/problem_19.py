# Function sum_of_list(numbers) that uses a loop to calculate and return total sum.
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_of_list([10, 20, 30, 40, 50]))
