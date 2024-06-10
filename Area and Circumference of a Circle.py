import math

radius = float(input("What is the radius of the circle?: "))
area = math.pi * radius **2

circumference = 2 * math.pi * radius

print("The area of the circle is "+str(area))
print("The circumference of the circle is "+str(circumference))