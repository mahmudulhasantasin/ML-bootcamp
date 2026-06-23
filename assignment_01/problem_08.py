# Compare a==b, a is b, c==d, c is d for ints and lists. Explain why == and 'is' differ for lists.
a, b = 15, 15
c, d = [1, 2], [1, 2]
print(a == b)
print(a is b)
print(c == d)
print(c is d)
