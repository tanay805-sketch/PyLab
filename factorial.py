n = int(input("Enter the number : "))


def factorial(n):
    facto = 1
    for i in range(1 , n+1):
        
        facto = facto*i

    return facto 

print(factorial(n))


