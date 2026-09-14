# Input a list from user and reverse it without using reverse() or slicing

n = int(input("Enter number of elements: "))
items = []
print("Enter elements:")
for i in range(n):
    items.append(input())

left = 0
right = n - 1

while left < right:
    temp = items[left]
    items[left] = items[right]
    items[right] = temp
    left += 1
    right -= 1

print("Reversed list:", items)
