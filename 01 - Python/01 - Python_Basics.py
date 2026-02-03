#Python print statement
print("HI") #use print to print
print("""this is me 
I am going to bed
and how are you""") #use """""" for multiline statements


a = 3 #variable initialization
print(a)
name = input("Enter your name: ") #user input
print(name)

a = int(input("Enter a number: ")) #take an integer as an input
print(a)

c = float(input("Enter a number: ")) #take a floating point number as input
print(c)

b = eval(input(2+3)) #Evaluate statements
print(b)

f = eval(input("Enter a number: "))
print(f)

# Problem 1 - Take variables for name, age and address and print the variables
name = "Ram"
age = 21
address = "fdhfhfa"

print(name)
print(age)
print(address)

#Problem 2 - Swap 2 numbers
a = 4
b = 5
print(a,b)

#Method 1
c = a
a = b
b = c
print(a)
print(b)

#Method 2
a,b = 1,2
a = a+b #a+=b
b = a-b #b = a-b
a = a-b #a-=b
print(a, b)

#Method 3
a, b = 1,2
a, b = b, a
print(a, b)

#Problem 3 - Student ID card
print("Student ID card.")
name = input("Enter your name: ")
grade = input("Enter your grade: ")
age = int(input("Enter your age: "))
phone_no = int(input("Enter your phone number: "))
email = input("Enter your email address: ")
print("Details")
print("Name:", name)
print("Grade:", grade)
print("Age:", age)
print("Phone number:", phone_no)
print("Email address:", email)

#Problem 4 - Check whether a number is positive or not
a = 3
if(a > 0):
    print("Positive")
elif(a==0):
    print("Zero")
else:
    print("Negative")

#Problem 5 - Check whether a number is even or odd
a = 0
if(a//2==0):
    print("Even")
else:
    print("Odd")

#Problem 6 - Creata an area calculator
print("****AREA Calculator****")
print("Press 1 to get area of square\n Press 2 to get area of rectangle \n Press 3 to get area of circle\n Press 4 to get area of triangle")
choice = int(input("Enter the number b/w 1 to 4 (1,2,3,4): "))
if choice == 1:
    side = float(input("Enter the side of square: "))
    area = side ** 2
    print(area)
elif choice == 2:
    length = float(input("Enter the length of rectangle: "))
    breadth = float(input("Enter the breadth of rectangle: "))
    area = length * breadth
elif choice == 3:
    radius = float(input("Enter the radius of circle: "))
    pie = 3.14
    area = pie * radius ** 2
    print(area)
elif choice == 4:
    base = float(input("Enter the base of triangle:"))
    height = float(input("Enter the height of triangle:"))
    area = 0.5 * base * height
else:
    print("Invalid choice. Please select a value between 1 and 4...")

#Problem 7 - Check if a letter is present in a string
a = "Hello"
b = input("Enter a letter to check if it is present in the string: ")

if (b in a) and (b in "aeiouAEIOU"):
    print(b, " is present in the string and is vowel.")
elif (b in a) and (b not in "aeiouAEIOU"):
    print(b, " is present in the string but is not a vowel.")
else:
    print(b, " is not present in the string.")

#Problem 8 - Check if a number is a single digit or a double digit
number = int(input("Enter a number: "))
if (number >=0 and number<10):
    print("Number is a single digit number.")
elif (number >=10 and number <=99):
    print("Number is a 2 digit number.")
else:
    print("Number is more than a 3 digit number")

