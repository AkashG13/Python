#Check a triangle is equilateral, isosceles or scalene


print("Input lengths of the triangle sides: ")
x,y,z=input().split()
if x == y == z:
	print("Equilateral triangle")
elif x==y or y==z or z==x:
	print("isosceles triangle")
else:
	print("Scalene triangle")
