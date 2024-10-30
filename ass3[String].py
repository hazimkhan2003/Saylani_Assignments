#  1. Write a program that accepts a string from user. Your program should count and display number of 
# vowels in that string. 
string = input("Enter a string: ")
vowels = 'aeiouAEIOU'
count = sum(1 for char in string if char in vowels)
print(f"Number of vowels in the string: {count}")

#  2. Write a program that reads a string from keyboard and display: 
# * The number of uppercase letters in the string 
# * The number of lowercase letters in the string 
# * The number of digits in the string 
# * The number of whitespace characters in the string 
string = input("Enter a string: ")

uppercase_count = sum(1 for char in string if char.isupper())
lowercase_count = sum(1 for char in string if char.islower())
digit_count = sum(1 for char in string if char.isdigit())
whitespace_count = sum(1 for char in string if char.isspace())

print(f"Uppercase letters: {uppercase_count}")
print(f"Lowercase letters: {lowercase_count}")
print(f"Digits: {digit_count}")
print(f"Whitespace characters: {whitespace_count}")

#  3. Write a Python program that accepts a string from user. Your program should create and display a 
# new string where the first and last characters have been exchanged. 
# For example if the user enters the string 'HELLO' then new string would be 'OELLH' 
string = input("Enter a string: ")

if len(string) > 1:
    new_string = string[-1] + string[1:-1] + string[0]
else:
    new_string = string  # if string has only one character

print(f"New string with first and last characters exchanged: {new_string}")

#  4. Write a Python program that accepts a string from user. Your program should create a new string in 
# reverse of first string and display it. 
# For example if the user enters the string 'EXAM' then new string would be 'MAXE' 
string = input("Enter a string: ")
reversed_string = string[::-1]
print(f"Reversed string: {reversed_string}")

#  5. Write a Python program that accepts a string from user. Your program should create a new string by 
# shifting one position to left. 
# For example if the user enters the string 'examination 2021' then new string would be 'xamination 
# 2021e' 
string = input("Enter a string: ")
shifted_string = string[1:] + string[0]
print(f"Shifted string: {shifted_string}")

#  6. Write a program that asks the user to input his name and print its initials. Assuming that the user 
# always types first name, middle name and last name and does not include any unnecessary spaces. 
# For example, if the user enters Ajay Kumar Garg the program should display A. K. G. 
# Note:Don't use split() method 
name = input("Enter your full name: ")

initials = ""
initials += name[0] + ". "  # First initial
for i in range(1, len(name)):
    if name[i] == " " and i + 1 < len(name):  # After space, take next character
        initials += name[i + 1] + ". "

print(f"Initials: {initials}")

# 7. A palindrome is a string that reads the same backward as forward. For example, the words dad, 
# madam and radar are all palindromes. Write a programs that determines whether the string is a 
# palindrome. 
# Note: do not use reverse() method 
string = input("Enter a string: ")
is_palindrome = string == string[::-1]

if is_palindrome:
    print(f"The string '{string}' is a palindrome.")
else:
    print(f"The string '{string}' is not a palindrome.")

# 8. Write a program that display following output: 
# SHIFT 
# HIFTS 
# IFTSH 
# FTSHI 
# TSHIF 
# SHIFT 
string = "SHIFT"

for i in range(len(string)):
    shifted_string = string[i:] + string[:i]
    print(shifted_string)

#  9. Write a program in python that accepts a string to setup a passwords. Your entered password must 
# meet the following requirements: 
# The password must be at least eight characters long. 
# It must contain at least one uppercase letter. 
# It must contain at least one lowercase letter. 
# It must contain at least one numeric digit. 
# Your program should should perform this validation.
password = input("Enter a password: ")

if len(password) >= 8 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password):
    print("Password is valid.")
else:
    print("Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, and one numeric digit.")
