# Take 7 integers from user and find smallest and largest without min() or max()

numbers = []
print("Enter 7 integers:")
for i in range(7):
    val = int(input())
    numbers.append(val)

smallest = numbers[0]
largest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print("List:", numbers)
print("Smallest:", smallest)
print("Largest:", largest)
