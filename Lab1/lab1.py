#Question 1
# a = [10, 20, 30, 20, 40, 50]
# a.remove(20)
# print(a)
#=============================================================================================================
#Question 2
# a = [10, 20, 30, 20, 40, 50]
# val=a.pop(1)
# print(a)
# print(val)
#=============================================================================================================
#Question 3
# a = [10, 20, 30, 40, 50, 60, 70]
# del a[1:4]
# print(a)
#=============================================================================================================
#Question 4
# a = [10, 20, 30, 40, 50, 60, 70]
# a.clear()
# print(a)
#=============================================================================================================
#Question 5
# Write a program that prints the number of times the substring 'iti' occurs in a string
# string="iti"
# val=string.count("i")
# print(val)
#=============================================================================================================
#Question 6
#application to take a number in binary form from the user, and print it as a decimal
# num=input("Enter a number in binary form: ")
# print(int(num,2))
#=============================================================================================================
#Question 7
#write a code take a number as an argument and if the number divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is divisible by both return "FizzBuzz"
# num=int(input("Enter a number: "))
# if num%3==0 and num%5==0:
#     print("FizzBuzz")
# elif num%3==0:
#     print("Fizz")
# elif num%5==0:
#     print("Buzz")
# else:
#     print(num)
#=============================================================================================================
#Question 8
#Ask the user to enter the radius of a circle print its calculated area and circumference
# x=input("Enter the radius of a circle: ")
# x=float(x)
# area=3.14*x*x
# circumference=2*3.14*x
# print("Area = ",area)
# print("Circumference = ",circumference)
#=============================================================================================================
#Question 9
#Ask the user for his name then confirm that he has entered his name (not an empty string/integers).then proceed to ask him for his email and print all this data
# name=input("Enter your name: ")
# if(name and name.isalpha()):
#   email=input("Enter your email: ")
#   print("Name: ",name)
#   print("Email: ",email)  
# else:
#   print("Invalid name")