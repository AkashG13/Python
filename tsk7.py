#Find the median of three values

a,b,c=input("Enter3 nos. to find median:").split()
if a>b and a<c:
    med=a
elif b>a and b<c:
    med=b
else:
    med=c
print("Median is: ",med)    
