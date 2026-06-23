# Assign 10,20,30 to a,b,c in one line. Swap a and c without temp variable.
a, b, c = 10, 20, 30
print("Before swap:", a, b, c)
a, c = c, a
print("After swap:", a, b, c)
