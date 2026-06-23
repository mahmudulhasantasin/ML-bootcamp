# Check whether a given word is present inside a sentence.
sentence = input("Enter a sentence: ")
word = input("Enter a word: ")
if word in sentence:
    print("Found")
else:
    print("Not found")
