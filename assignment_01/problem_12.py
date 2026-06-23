# Split 'Data,Science,Machine,Learning' by comma, print list, 2nd element, count, join with ' -> '.
text = 'Data,Science,Machine,Learning'
words = text.split(',')
print(words)
print(words[1])
print(len(words))
print(' -> '.join(words))
