#Write a python program to count the number of even and odd numbers from a series of numbers.

a=[]
print("Enter no. of elements of list:")
n=int(input())
for i in range(0,n):
    print("Enter %dth element: "%(i+1))
    element=int(input())
    a.append(element)
print("list is: ",a)
Odd_count=0
Even_count=0
for j in range(n):
    if(a[j]%2 == 0):
        Even_count = Even_count + 1
    else:
        Odd_count = Odd_count + 1

print("\nTotal Number of Even Numbers in this List =  ", Even_count)
print("Total Number of Odd Numbers in this List = ", Odd_count)

