numbers = [10, 20, 30, 40, 50]

n = int(input("Enter element to remove: "))

if n in numbers:
    numbers.remove(n)
    print("Updated list:", numbers)
else:
    print("Element not found")