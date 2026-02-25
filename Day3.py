# Declare your age as integer variable
age =  24
# Declare your height as a float variable
height = 183
# Declare a variable that store a complex number
comp = 5 + 1j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#     Enter base: 20
#     Enter height: 10
#     The area of the triangle is 100
base=   int(input('Enter Base:  '))
height = int(input('Enter Height:  '))
area = 0.5 * base * height 
print(area)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# Enter side a: 5
# Enter side b: 4
# Enter side c: 3
# The perimeter of the triangle is 12

a = int(input("enter side a: "))
b = int(input("enter side b: "))
c = int(input("enter side c: "))
perimeter = a+b+c
print(perimeter)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

length = int(input("enter the length: "))
width =int(input("enter width:  "))
perimeter = 2 * (length + width)
print (perimeter)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
import math
r = int(input("Enter radius : "))
radius = 2 * math.pi* r
print (radius)


# Calculate the slope, x-intercept and y-intercept of y = 2x -2

# y-intercept occurs when x = 0
y_intercept = -2

# x-intercept occurs when y = 0
# 0 = 2x - 2  =>  2x = 2  =>  x = 1
x_intercept = 1

slope2= 2
# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1,x2=2,10
y2,y1=2,2
slope1 = (y2-y1)//(x2-x1)


# Compare the slopes in tasks 8 and 9.
print (slope1 > slope2)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print (not (len('python') != len('dragon')))
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print ('on' in 'dragon','on' in 'python')

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("jargon" in "I hope this course is not full of jargon" )
# There is no 'on' in both dragon and python
print ('on' in 'dragon' and 'on' in 'python')
# Find the length of the text python and convert the value to float and convert it to string
print(type(len("python") ))
print(type(float(len("python"))))
print(type(str(len("python")) ))


# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
print( 4%2 == 0)
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print((7/1/3) == int(2.7))
# Check if type of '10' is equal to type of 10
print(type('10') == type(10) )
# Check if int('9.8') is equal to 10

print(int(9.8) == 10)

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120
hours= float(input("Enter hours: "))
rate=float(input("Enter rate per hour: "))
earning= hours * rate
print("Your weekly earning is: " + str(earning))

# Write a script that prompts the user to enter number of years. 
# Calculate the number of seconds a person can live.
#  Assume a person can live hundred years
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.
years = float(input("Enter number of years you have lived: "))
print("you have lived: " + str(3600 * years ) + "secounds")


# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
print(1, 1**0, 1**1, 1**2, 1**3)
print(2, 2**0, 2**1, 2**2, 2**3)
print(3, 3**0, 3**1, 3**2, 3**3)
print(4, 4**0, 4**1, 4**2, 4**3)
print(5, 5**0, 5**1, 5**2, 5**3)

# i know we need to use a for loop but its day 3 :)

# Display the table

for i in range(1, 6):
    print(i, i**0, i**1, i**2, i**3)

# 🎉 CONGRATULATIONS ! 🎉