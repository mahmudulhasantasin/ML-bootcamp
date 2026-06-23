# Strip s='  python programming  ', then show stripped, upper(), title(), replace('python','data'), and length.
s = '  python programming  '
stripped = s.strip()
print(stripped)
print(stripped.upper())
print(stripped.title())
print(stripped.replace('python', 'data'))
print(len(stripped))
