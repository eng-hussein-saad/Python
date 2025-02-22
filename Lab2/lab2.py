#Question 1 :
#Write a simple calculator program using match to perform addition, subtraction, multiplication, and division.
# num1=int(input("Enter the first number: "))
# num2=int(input("Enter the second number: "))
# operator=input("Enter the operator: ")
# match operator:
#   case "+":
#     print(num1+num2)
#   case "-":
#     print(num1-num2)
#   case "*":
#     print(num1*num2)
#   case "/":
#     if num2==0:
#       print("can't divide by zero")
#     else:
#       print(num1/num2)
#   case _:
#     print("Invalid operator")
#==========================================================================================================================
#Question 2 :
#Write a program to filter out even numbers from a list and count how many are left.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = []
# for num in numbers:
#   if num%2==0:
#     even_numbers.append(num)
# print(f"{even_numbers=}")
# print(f"count of numbers left is {len(numbers) - len(even_numbers)}")
#==========================================================================================================================
#Question 3 :
# Write a program to check if a password meets the following criteria:
# - At least 8 characters long.
# - Contains at least one uppercase letter.
# - Contains at least one digit.
#first solution
# password=input("Enter the password: ")
# is_uppercase=False
# is_digit=False
# if len(password)>=8:
#   for char in password:
#     if char.isupper():
#       is_uppercase=True
#     elif char.isdigit():
#       is_digit=True
#   if is_uppercase and is_digit:
#     print("password is valid")
#   elif not(is_uppercase) and not(is_digit):
#     print("Password should contain at least one uppercase letter and one digit")
#   elif not(is_uppercase):
#     print("Password should contain at least one uppercase letter")
#   elif not(is_digit):
#     print("Password should contain at least one digit")
#   else:
#     print("password should contain at least one uppercase letter and one digit")
# else:
#   print("password should contain at least 8 characters")
#=====================================================================
#second solution (pythonic way):
# password=input("Enter the password: ")
# if len(password)>=8 and any(char.isupper() for char in password) and any(char.isdigit() for char in password):
#   print("password is valid")
# else:
#   print("password should contain at least 8 characters and at least one uppercase letter and one digit")
#=========================================================================================================================
#Question 4: 
#Write a Python script to concatenate the following dictionaries to create a new one.
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4={**dic1, **dic2, **dic3}
# print(dic4)
#==========================================================================================================================
#Question 5:
#takes a string and prints the longest alphabetical ordered substring occured.For example,
# if the string is 'abdulrahman' then the output is:
#Longest substring in alphabetical order is: abdu

# s="zyabcde"
# longest = current = s[0]  
# for i in range(1, len(s)):
#   if s[i] >= s[i - 1]: 
#     current += s[i]
#   else:
#     if len(current) > len(longest):  
#       longest = current
#     current = s[i]  # Reset current substring
    
    
# if len(current) > len(longest):
#   longest = current
# print(f"Longest substring in alphabetical order is: {longest}")
#==========================================================================================================================
#Question 6:
#Write a program to check if a Email meets the following criteria:
  #Ensures the email follows a standard format (e.g., local@domain.com).
  #Does not check if the email actually exists or is deliverable.
import re
email=input("Enter the email: ")
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
print("valid email") if bool(re.match(pattern, email)) else print("invalid email")