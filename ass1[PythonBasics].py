# Print Your Name with your Father name and Date of birth using suitable escape sequence charactor
print("Name: John Doe\nFather's Name: Mr. Doe\nDate of Birth: 01\\01\\2000")

# Write your small bio using variables and print it using print function
name = "John Doe"
age = 24
profession = "Software Engineer"
hobby = "Reading"

print(f"My name is {name}. I am {age} years old. I work as a {profession}, and I enjoy {hobby}.")

# Write a program in which use all the operators we can use in Python
# # Write your code here
a = 10
b = 3

# Arithmetic Operators
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
modulus = a % b
exponentiation = a ** b
floor_division = a // b

# Assignment Operators
c = 5
c += 3

# Comparison Operators
is_equal = (a == b)
is_greater = (a > b)
is_less = (a < b)

# Logical Operators
logical_and = (a > 5 and b < 5)
logical_or = (a > 5 or b < 1)

# Bitwise Operators
bitwise_and = a & b
bitwise_or = a | b
bitwise_xor = a ^ b

# Identity Operators
is_same = (a is b)

# Membership Operators
list_of_numbers = [1, 2, 3, 10]
is_member = (a in list_of_numbers)

print("All operations completed.")

# Completes the following steps of small task:
# Mention Marks of English , Islamiat and Maths out of 100 in 3 different variables
# Mention Variable of Total Marks and assign 300 to it
# Calculate Percentage
# # Write your code here
english = 85
islamiat = 90
maths = 95
total_marks = 300
obtained_marks = english + islamiat + maths
percentage = (obtained_marks / total_marks) * 100
print(f"Total Marks: {obtained_marks}, Percentage: {percentage:.2f}%")

# Part -2 Python Basics (Conditional Statements)
# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.
# #Type your code here
salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))

if years_of_service > 5:
    bonus = salary * 0.05
    print(f"Bonus Amount: {bonus}")
else:
    print("No bonus.")

# Write a program to check whether a person is eligible for voting or not. (accept age from user) if age is greater than 17 eligible otherwise not eligible
# #Type your code here
age = int(input("Enter your age: "))
if age > 17:
    print("Eligible for voting.")
else:
    print("Not eligible for voting.")

# Write a program to check whether a number entered by user is even or odd.
# #Type your code here
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even number.")
else:
    print("Odd number.")

# Write a program to check whether a number is divisible by 7 or not. Show Answer
# #Type your code here
number = int(input("Enter a number: "))
if number % 7 == 0:
    print(f"{number} is divisible by 7.")
else:
    print(f"{number} is not divisible by 7.")

# Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye".
# #Type your code here
number = int(input("Enter a number: "))
if number % 5 == 0:
    print("Hello")
else:
    print("Bye")

# Write a program to display the last digit of a number.
# #Type your code here
number = int(input("Enter a number: "))
last_digit = number % 10
print(f"Last digit: {last_digit}")

# Take values of length and breadth of a rectangle from user and print if it is square or rectangle.
# #Type your code here 
length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))

if length == breadth:
    print("It is a square.")
else:
    print("It is a rectangle.")

# Take two int values from user and print greatest among them.
# # Type your code here
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(f"The greatest number is: {num1}")
else:
    print(f"The greatest number is: {num2}")

# A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.
# #Type your code here
quantity = int(input("Enter quantity: "))
unit_price = 100
total_cost = quantity * unit_price

if total_cost > 1000:
    total_cost -= total_cost * 0.10

print(f"Total cost: {total_cost}")

# A school has following rules for grading system:
# a. Below 25 - F

# b. 25 to 45 - E

# c. 45 to 50 - D

# d. 50 to 60 - C

# e. 60 to 80 - B

# f. Above 80 - A

# Ask user to enter marks and print the corresponding grade.
# #Type your code here
marks = int(input("Enter your marks: "))

if marks < 25:
    print("Grade: F")
elif 25 <= marks < 45:
    print("Grade: E")
elif 45 <= marks < 50:
    print("Grade: D")
elif 50 <= marks < 60:
    print("Grade: C")
elif 60 <= marks < 80:
    print("Grade: B")
else:
    print("Grade: A")

# 14)A student will not be allowed to sit in exam if his/her attendence is less than 75%.

# Take following input from user

# Number of classes held

# Number of classes attended.

# And print

# percentage of class attended

# Is student is allowed to sit in exam or not.

# #Type your code here
total_classes = int(input("Enter total number of classes held: "))
attended_classes = int(input("Enter number of classes attended: "))

attendance_percentage = (attended_classes / total_classes) * 100
print(f"Attendance Percentage: {attendance_percentage}%")

if attendance_percentage >= 75:
    print("Allowed to sit in exam.")
else:
    print("Not allowed to sit in exam.")


# Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.
# #Type your code here
total_classes = int(input("Enter total number of classes held: "))
attended_classes = int(input("Enter number of classes attended: "))
medical_cause = input("Do you have a medical cause (Y/N)? ")

attendance_percentage = (attended_classes / total_classes) * 100

if attendance_percentage >= 75 or medical_cause.lower() == 'y':
    print("Allowed to sit in exam.")
else:
    print("Not allowed to sit in exam.")

# Write a program to check if a year is leap year or not.
# If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.
# #Type your code here
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.

# if employee is a male and age is in between 20 to 40 then he may work in anywhere

# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

# And any other input of age should print "ERROR"
# #Type your code here
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
marital_status = input("Enter your marital status (Y/N): ")

if gender == 'F':
    print("Work in urban areas only.")
elif gender == 'M' and 20 <= age <= 40:
    print("Can work anywhere.")
elif gender == 'M' and 40 <= age <= 60:
    print("Work in urban areas only.")
else:
    print("ERROR")

# Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria : Unit Price
# uptp 100 units no charge Next 200 units Rs 5 per unit After 200 units Rs 10 per unit (For example if input unit is 350 than total bill amount is Rs.3500 (For example if input unit is 97 than total bill amount is Rs.0 (For example if input unit is 150 than total bill amount is Rs.750
units = int(input("Enter number of units: "))
bill = 0

if units <= 100:
    bill = 0
elif units <= 300:
    bill = (units - 100) * 5
else:
    bill = (200 * 5) + (units - 300) * 10

print(f"Total bill amount: Rs.{bill}")

# Take input of age of 3 people by user and determine oldest and youngest among them.
# #Type your code here
age1 = int(input("Enter the age of person 1: "))
age2 = int(input("Enter the age of person 2: "))
age3 = int(input("Enter the age of person 3: "))

oldest = max(age1, age2, age3)
youngest = min(age1, age2, age3)

print(f"The oldest person is {oldest} years old.")
print(f"The youngest person is {youngest} years old.")
