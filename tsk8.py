#Write a python function to multiply all the numbers in a list
def multiply(numbers):  
    total = 1
    for n in numbers:
        total *= n  
    return total  
a=[]
print("Enter no. of elements of list:")
n=int(input())
for i in range(0,n):
    print("enter elements of list")
    element=int(input())
    a.append(element)
    print(a)
print(multiply(a))
