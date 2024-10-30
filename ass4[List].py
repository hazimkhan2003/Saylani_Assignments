# 1. Write a program that accepts a list from user and print the alternate element of list. 
user_list = input("Enter a list of elements separated by spaces: ").split()
print("Alternate elements of the list are:")
print(user_list[::2])

# 2. Write a program that accepts a list from user. Your program should reverse the content of list and 
# display it. Do not use reverse() method. 
user_list = input("Enter a list of elements separated by spaces: ").split()
reversed_list = user_list[::-1]
print("Reversed list is:", reversed_list)

#  3. Find and display the largest number of a list without using built-in function max(). Your program 
# should ask the user to input values in list from keyboard. 
user_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
largest = user_list[0]
for num in user_list:
    if num > largest:
        largest = num
print("The largest number in the list is:", largest)

#  4. Write a program that rotates the element of a list so that the element at the first index moves to the 
# second index, the element in the second index moves to the third index, etc., and the element in the last 
# index moves to the first index. 
user_list = input("Enter a list of elements separated by spaces: ").split()
rotated_list = user_list[1:] + user_list[:1]
print("Rotated list is:", rotated_list)

# 5. Write a program that input a string and ask user to delete a given word from a string. 
string = input("Enter a string: ")
word_to_delete = input("Enter the word to delete: ")
new_string = string.replace(word_to_delete, "")
print("Updated string:", new_string)

#  6. Write a program that reads a string from the user containing a date in the form mm/dd/yyyy. It 
# should print the date in the form March 12, 2021. 
date = input("Enter a date in mm/dd/yyyy format: ")
month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
mm, dd, yyyy = map(int, date.split('/'))
formatted_date = f"{month_names[mm - 1]} {dd}, {yyyy}"
print("Formatted date:", formatted_date)

#  7. Write a program with a function that accepts a string from keyboard and create a new string after 
# converting character of each word capitalized. For instance, if the sentence is "stop and smell the roses." 
# the output should be "Stop And Smell The Roses" 
def capitalize_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

sentence = input("Enter a sentence: ")
capitalized_sentence = capitalize_words(sentence)
print("Capitalized sentence:", capitalized_sentence)

# 8. Find the sum of each row of matrix of size m x n. For example for the following matrix output will be 
# like this : 
# Sum of row 1 = 32 
# Sum of row 2 = 31 
# Sum of row 3 = 63 
rows = int(input("Enter the number of rows: "))
matrix = []

for i in range(rows):
    row = list(map(int, input(f"Enter row {i + 1} elements separated by spaces: ").split()))
    matrix.append(row)

for i, row in enumerate(matrix):
    print(f"Sum of row {i + 1} =", sum(row))

# 9. Write a program to add two matrices of size n x m. 
rows, cols = map(int, input("Enter the number of rows and columns for the matrices: ").split())
matrix1 = []
matrix2 = []

print("Enter elements of matrix 1:")
for i in range(rows):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    matrix1.append(row)

print("Enter elements of matrix 2:")
for i in range(rows):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    matrix2.append(row)

result_matrix = []
for i in range(rows):
    result_row = [matrix1[i][j] + matrix2[i][j] for j in range(cols)]
    result_matrix.append(result_row)

print("Sum of the two matrices is:")
for row in result_matrix:
    print(row)

# 10. Write a program to multiply two matrices
rows1, cols1 = map(int, input("Enter rows and columns of first matrix: ").split())
rows2, cols2 = map(int, input("Enter rows and columns of second matrix: ").split())

if cols1 != rows2:
    print("Multiplication not possible. The number of columns in the first matrix must be equal to the number of rows in the second matrix.")
else:
    print("Enter elements of matrix 1:")
    matrix1 = [list(map(int, input(f"Row {i + 1}: ").split())) for i in range(rows1)]

    print("Enter elements of matrix 2:")
    matrix2 = [list(map(int, input(f"Row {i + 1}: ").split())) for i in range(rows2)]

    # Initialize the result matrix with zeros
    result_matrix = [[0] * cols2 for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    print("Product of the two matrices is:")
    for row in result_matrix:
        print(row)
