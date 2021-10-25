# Task 1
import math

x = int(input("x="))
if x % 2 != 0:
    print("x is odd")
else:
    print("x is even")
if x % 20 == 0:
    print("is a multiple of 20")
else:
    print("x is  not a multiple of 20")

print()

x = int(input("x="))
y = int(input("y="))

if x >= 0 and y >= 0:
    print("Both positive")
else:
    print("Are not both positive")

if (x >= 0 and y >= 0) or (x < 0 and y < 0):
    print("x and y have the same sign")
else:
    print("x and y have different signs")

x = int(input("x="))
y = int(input("y="))
z = int(input("z="))

if x == y == z:
    print("Same value")
else:
    print("Different value")

if (x != y) and (x != z) and (y != z):
    print("Different values")
else:
    print("Same value somewhere")

if (x == y and x != z) or (x == z and x != y) or (y == z and y != x):
    print("two values are the same and other is not")
else:
    print("Bruh")

x1 = int(input("x1="))
y1 = int(input("y1="))
x2 = int(input("x2="))
y2 = int(input("y2="))

dis = math.sqrt((x1-x2)**2 + (y1-y2)**2)
print(dis)

slope = (y2-y1)/(x2-x1)
print(slope)

if x1 == x2 == 0 or y1 == y2 == 0:
    print("both points lie on same line on origin")
else:
    print("points dont lie on same line of origin")

if y1 > y2:
    print("First point is higher")
else:
    print("First point is not higher")

if x1 >= 0 and y1 >= 0:
    print("First")
elif x1 < 0 <= y1:
    print("Second")
elif x1 < 0 and y1 < 0:
    print("Third")
else:
    print("Fourth")

# checking if coordinates have same sign in according axis
if abs(x1 + x2) == abs(x1) + abs(x2) and abs(y1 + y2) == abs(y1) + abs(y2):
    print("Same quadrant")
else:
    print("Different quadrant")
