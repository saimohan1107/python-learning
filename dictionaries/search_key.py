student = {
    "name": "Sai",
    "age": 19,
    "course": "CSE"
}

key = input("Enter key to search: ")

if key in student:
    print("Key found")
else:
    print("Key not found")