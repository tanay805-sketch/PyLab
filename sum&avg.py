# Take 10 integers from user, store in list, then find sum and average without sum()

numbers = []
print("Enter 10 integers:")
for i in range(10):
    val = int(input())
    numbers.append(val)

total = 0
count = 0
for num in numbers:
    total += num
    count += 1

average = total / count

print("List:", numbers)
print("Sum:", total)
print("Average:", average)
