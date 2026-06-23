# For 'Banana': find('a'), count('a'), startswith('Ba'), endswith('na'), isdigit(). Also check '12345' vs '123a5'.
word = 'Banana'
print(word.find('a'))
print(word.count('a'))
print(word.startswith('Ba'))
print(word.endswith('na'))
print(word.isdigit())
print('12345'.isdigit())
print('123a5'.isdigit())
