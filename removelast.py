##wap to remove the last element of a list

def removelast():
    n = int(input("enter the sizd of the list : "))
    lst = []

    for i in range(1, n + 1):
        num = int(input(f"Enter number {i}: "))
        lst.append(num)

    print(lst)

    if lst: 
        lst.pop()
        print("List after removing the last element:", lst)
    else:
        print("The list is empty!")



removelast()
