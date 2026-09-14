# Input integers into a list and remove duplicates while preserving order

n = int(input("Enter number of elements: "))
numbers = []
print("Enter integers:")
for i in range(n):
    numbers.append(int(input()))

unique_numbers = []
for num in numbers:
    is_duplicate = False
    for item in unique_numbers:
        if item == num:
            is_duplicate = True
            break
    if not is_duplicate:
        unique_numbers.append(num)

print("Original list:", numbers)
print("List without duplicates:", unique_numbers)
