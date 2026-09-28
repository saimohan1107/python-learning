text = input("Enter a string: ")
word = input("Enter word to search: ")

if word in text:
    print("Word found")
else:
    print("Word not found")