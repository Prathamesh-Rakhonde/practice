
# #! | Exception Name      | Cause                                         | Example                           |
# #? | ------------------- | --------------------------------------------- | --------------------------------- |
# #^ | `ZeroDivisionError` | Dividing a number by zero                     | `x = 5 / 0`                       |
# #^ | `ValueError`        | Invalid value passed to a function            | `int("abc")`                      |
# #^ | `TypeError`         | Unsupported operation or wrong data type      | `len(5)`                          |
# #^ | `IndexError`        | Accessing invalid index in a list/tuple       | `lst = [1,2]; lst[5]`             |
# #^ | `KeyError`          | Accessing a dictionary key that doesn't exist | `d = {'a':1}; d['b']`             |
# #^ | `FileNotFoundError` | Trying to open a file that doesn’t exist      | `open('nofile.txt')`              |
# #^ | `AttributeError`    | Accessing invalid attribute of an object      | `'hello'.append('!')`             |
# #^ | `ImportError`       | Importing a module that doesn’t exist         | `import some_nonexistent_module`  |
# #^ | `IndentationError`  | Incorrect indentation                         | Bad indentation in code           |
# #^ | `NameError`         | Using a variable that hasn’t been defined     | `print(x)` where `x` is undefined |

# ##!=================================================================================================

# ##! 🟢 Easy Level

# # 1.Check if a number is even or odd.
# # 2.Check if a number is positive, negative, or zero.
# # 3.Check if a person is eligible to vote (age ≥ 18).
# # 4.Check whether a character is a vowel or consonant.
# # 5.Check if a given year is a leap year.
# # 6.Find the maximum of two numbers.
# # 7.Check if a number is divisible by 5 and 11.

# ##^=============================================================================================

# ##! 1.Check if a number is even or odd.

# def evod(num) :
#     if num % 2 == 0 :
#         print(f"Number {num} is a even number")
#     else :
#         print(f"Number {num} is a odd number")
# try :
#     evod(num = int(input("Enter no. to check it's eve or odd = ")))
# except ValueError :
#     print("Entered value must be integer type only.")

# ##^=================================================================================================

# ##! 2.Check if a number is positive, negative, or zero.

# def posneg(num) :
#     if num >= 0 :
#         print(f"Number {num} is a positive number.")
#     else :
#         print(f"Number {num} is a negative number.")
# try :
#     num = int(input("Enter a number to check its positive or negative = "))
#     posneg(num)
# except ValueError :
#     print("Entered value must be integer type only.")

# ##^=================================================================================================

# ##! 3.Check if a person is eligible to vote (age ≥ 18).

# def vote(age) :
#     if age >= 18 :
#         print("Your eligible to vote.")
#     elif age >= 15 and age < 18 :
#         print("Wait few years to vote champ.")
#     else :
#         print("Not eligible to vote")
# try :
#     age = int(input("Enter your age here : "))
#     vote(age)
# except ValueError:
#     print("Input must be Integer type only. Please try again.")

# ##^=================================================================================================

# ##! 4.Check whether a character is a vowel or consonant

# def voco(char) :

#     if char in ['a','e','i','o','u'] :
#         print(f"{char} is a vowel.")
#     else :
#         print(f"{char} is consonant.")

# char = input("Enter character to check its vowel or consonant : ").lower()
# voco(char)

# #& Check whether a character is a vowel or consonant UPDATED
# def voco(char):

#     if len(char) != 1 :
#         print("Please enter a single alphabet character only.")
#     elif not char.isalpha():
#         print("Enter character only.")
#     elif char in ['a', 'e', 'i', 'o', 'u']:
#         print(f"{char} is a vowel.")
#     else:
#         print(f"{char} is a consonant.")

# char = input("Enter a character to check if it's a vowel or consonant: ").lower()
# voco(char)

# ##^=================================================================================================


# ##! 5.Check if a given year is a leap year.

# def leap(year):
#     if year % 400 == 0:
#         print(f"{year} is a leap year.")
#     elif year % 100 == 0:
#         print(f"{year} is not a leap year.")
#     elif year % 4 == 0:
#         print(f"{year} is a leap year.")
#     else:
#         print(f"{year} is not a leap year.")
# try :
#     year = int(input("Enter year : "))
#     leap(year)
# except ValueError :
#     print("Enter input of Integer typr only")

# #& Check if a given year is a leap year UPDATED.
# def leap(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(f"{year} is a leap year.")
#     else:
#         print(f"{year} is not a leap year.")

# try:
#     year = int(input("Enter year: "))
#     leap(year)
# except ValueError:
#     print("Enter input of Integer type only.")

# ##^=================================================================================================


# #! 6.Find the maximum of two numbers.

# def find_max(num1,num2) :
#     if num1 > num2 :
#         print(f"In {num1} and {num2} maximum number is {num1}")
#     elif num1 < num2 :
#         print(f"In {num1} and {num2} maximum number is {num2}")
#     else :
#         print(f"Both {num1} and {num2} are equal.")
# try :
#     print("Enter two numbers to find maximum number.")
#     num1 = int(input("Enter first number : "))
#     num2 = int(input("Enter second number : "))
#     find_max(num1,num2)
# except ValueError :
#     print("Please enter integer numbers only.")

# ##^=================================================================================================

# ##! 7.Check if a number is divisible by 5 and 11.

# def div(num) :
#     if num % 5 == 0 and num % 11 == 0 :
#         print(f"{num} is divisible by both 5 and 11.")
#     else :
#         print(f"{num} is not divisible both by 5 and 11.")
# try :
#     num = int(input("Enter a Number : "))
#     div(num)
# except ValueError :
#     print("Please enter integer numbers only.")

# ##^=================================================================================================
# ##!=================================================================================================

# ##! 🟡 Medium Level

# # 1.Find the largest among three numbers.
# # 2.Check if a character is an alphabet, digit, or special character.
# # 3.Grade calculator based on score input (A, B, C, etc.).
# # 4.Check if a triangle is valid given its three angles.
# # 5.Determine if a number is prime or not.
# # 6.Check whether a year is a century year (ends in 00) and if it's a leap century.
# # 7.Electricity bill calculator using if-else (based on unit ranges).

# ##^=================================================================================================

# ##! 1.Find the largest among three numbers.

# def lar(a, b, c):
#     if a >= b and a >= c:
#         print(f"{a} is the largest number.")
#     elif b >= a and b >= c:
#         print(f"{b} is the largest number.")
#     else:
#         print(f"{c} is the largest number.")

# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     c = int(input("Enter third number: "))
#     lar(a, b, c)
# except ValueError:
#     print("Input must be of integer type only.")

# ##^=================================================================================================

# ##! 2.Check if a character is an alphabet, digit, or special character.

# def check(char) :
#     if len(char) != 1:
#         print("Please enter exactly one character.")
#     elif char.isalpha() :
#         print(f"{char} is an alphabet.")
#     elif char.isdigit() :
#         print(f"{char} is a digit.")
#     else :
#         print("It's an special character.")

# char = input("Enter a character : ")
# check(char)

# ##^=================================================================================================

# ##! 3.Grade calculator based on score input (A, B, C, etc.).

# def grade(score) :
#     if 85 <= score <= 100:
#         print(f"{score} - You got an A grade.")
#     elif 55 <= score < 85:
#         print(f"{score} - You got a B grade.")
#     elif 35 <= score < 55:
#         print(f"{score} - You got a C grade.")
#     else:
#         print(f"{score} - Failed. Try again, don't give up.")
# score = input("Enter you'r score : ")
# if score.isdigit() :
#     score = float(score)
#     if 0 <= score <= 100:
#         grade(score)
#     else:
#         print("Score must be between 0 and 100. Please check your input.")
# else:
#     print("Invalid input. Please enter a numeric score.")

# ##^=================================================================================================

# ##! 4.Check if a triangle is valid given its three angles.

# def triangle(a1, a2, a3):
#     total = a1 + a2 + a3
#     if a1 <= 0 or a2 <= 0 or a3 <= 0:
#         print("Angles must be greater than 0. Invalid triangle.")
#     elif total == 180 :
#         print(f"The sum of angles {a1} + {a2} + {a3} = {total}. It's a valid triangle.")
#     else:
#         print(f"The sum of angles {a1} + {a2} + {a3} = {total}. This is not a valid triangle.")

# try:
#     print("Enter 3 angles to check if they form a valid triangle.")
#     a1 = int(input("Enter first angle: "))
#     a2 = int(input("Enter second angle: "))
#     a3 = int(input("Enter third angle: "))
    
#     triangle(a1, a2, a3)
# except ValueError:
#     print("Invalid input. Please enter integer values for angles.")

# ##^=================================================================================================

# ##! 5.Determine if a number is prime or not.

# def prime(num) :

#     if num < 0 :
#         print(f"{num} is negative. Prime numbers must be positive integers greater than 1.")
#     elif num == 0 or num == 1 :
#         print(f"{num} is neither prime nor composite.")
#     elif num == 2 :
#             print(f"{num} is a prime number.")
#     else :
#         for i in range (2,num) :
#             if num % 2 == 0 :
#                 print(f"{num} is not a prime number.")
#                 break
#             else :
#                 print(f"{num} is a prime number.")
#                 break

# try :
#     num = int(input("Enter a number to check it is prime or not : "))
#     prime(num)
# except ValueError :
#     print("Number must be Integer type only.")

# ##^=================================================================================================

# ##! 6.Check whether a year is a century year (ends in 00) and if it's a leap century.

# def check(year):
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap century year.")
#         else:
#             print(f"{year} is a century year, but not a leap year.")
#     else:
#         print(f"{year} is not a century year.")

# try:
#     year = int(input("Enter the year: "))
#     check(year)
# except ValueError:
#     print("Invalid input. Year must be an integer.")

# #^=================================================================================================

# #! 7.Electricity bill calculator using if-else (based on unit ranges).
 
# def calc(unit) :
#     if unit > 0 :
#         if unit <= 100 :
#             print(f"Your unit's are {unit} on that bases your bill becomes Rs.",unit*1.5)
#         elif unit <= 200 :
#             print(f"Your unit's are {unit} on that bases your bill becomes Rs.",(100*1.5)+(unit-100)*2.0)
#         elif unit <= 300 :
#             print(f"Your unit's are {unit} on that bases your bill becomes Rs.",(100*1.5)+(100*2.0)+(unit-200)*3.0)
#         else :
#             print(f"Your unit's are {unit} on that bases your bill becomes Rs.",(100*1.5)+(100*2.0)+(100*3.0)+(unit-300)*5.0)
# try :
#     unit = float(input("Enter your units here : "))
#     calc(unit)
# except ValueError :
#     print("Entered wrong units.")

# ##^=================================================================================================
# ##!=================================================================================================

# ##! 🔴 Hard Level
# # Simple login system with username/password validation.
# # ATM withdrawal simulation with balance checks and pin validation.
# # Nested if-else: Check if a student passed and assign grade based on marks in 5 subjects.
# # Time-based greeting (morning, afternoon, evening) using user-inputted hour.
# # Simulate a traffic light system – take light color as input and decide action.
# # Check if a triangle is scalene, isosceles, or equilateral based on side lengths.
# # Body Mass Index (BMI) calculator with health category output.

# ##^=================================================================================================