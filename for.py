
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

# ##! ✅ 🟢 Easy Level – Basic Looping (Print, Iterate)
# ##* 1. Print numbers from 1 to 10 using a for loop.
# ##* 2. Print even numbers between 1 and 50 using a while loop.
# ##* 3. Print the multiplication table of a given number (e.g., 7).
# ##* 4. Print characters of a string one by one using a for loop.
# ##* 5. Calculate the sum of numbers from 1 to n.
# ##* 6. Print all numbers from 10 to 1 (reverse counting).
# ##* 7. Print the first 10 odd numbers using a loop.

# ##^=================================================================================================

# ##! 1. Print numbers from 1 to 10 using a for loop.

# ##& Using for loop.
# for i in range(1,11) :
#     print(i)
#     # print(i,end=', ') ##* To print values in horizontal format seprated by comma (,).

# ##& Using while loop.
# i = 1
# while i < 11 : # Yes i can also use i<=10 condition here.
#     print(i)
#     # print(i,end='') ##* To print values in horizontal format.
#     i+=1

# ##^=================================================================================================


# ##! 2. Print even numbers between 1 and 50 using a while loop.

# ##& Using while loop.
# i = 2
# while i <= 50 :
#     print(i)
#     i += 2

# ##& Using for loop.
# for i in range(2,51,2) :
#     print(i,end=', ')

# ##^=================================================================================================

# ##! 3. Print the multiplication table of a given number (e.g., 7).

# ##& Using for loop.

# def table_with_for(num) :
#     for i in range(1,11) :
#         print(f"{num} * {i} = ",num*i)
# try :
#     num = int(input("Enter number to get its table : "))
#     table_with_for(num)
# except ValueError :
#     print("Number must be Integer type only.")

# ##& Using while loop.

# def table_with_while(num) :
#     i = 1
#     while i <= 10 :
#         print(f"{num} * {i} = ",num*i)
#         i+=1
# try :
#     num = int(input("Enter number to get its table : "))
#     table_with_while(num)
# except ValueError :
#     print("Number must be Integer type only.")

# ##^=================================================================================================

# #! 4. Print characters of a string one by one using a for loop.

# ##& Using for loop.

# def string_for(char) :
#     for i in char :
#         print(i)
# char = input("Enter youre string : ")
# string_for(char)

# ##& Using while loop.

# def string_while(char) :
#     i = 0
#     while i < len(char) :
#     # while i in range(len(char)) :
#         print(char[i])
#         i+=1
# char = input("Enter youre string : ")
# string_while(char)

# ##^=================================================================================================

# ##! 5. Calculate the sum of numbers from 1 to n.

# ##& Usinf for loop.

# def cal(num) :
#     s = 0
#     for i in range(num+1) :
#         s += i
#     print(f"Sum from 1 to {num} = {s}")
# try :
#     num = int(input("Enter a number : "))
#     cal(num)
# except ValueError :
#     print("Number must be integer type.")

# ##! Using formula
# s = num * (num + 1) // 2

# ##& Using while loop.

# def cal(num) :
#     s = 0
#     i = 1
#     while i <= num :
#         s += i
#         i += 1
#     print(f"Sum from 1 to {num} = {s}")
# try :
#     num = int(input("Enter a number : "))
#     cal(num)
# except ValueError :
#     print("Number must be integer type.")

# ##^=================================================================================================

# ##! 6. Print all numbers from 10 to 1 (reverse counting).

# ##& Using for loop.

# for i in range(10,0,-1) :
#     print(i)

# ##& Using while loop.

# i = 10
# while i >= 1 :
#     print(i)
#     i -= 1

# ##^=================================================================================================

# ##! 7. Print the first 10 odd numbers using a loop.

# ##& Using for loop.

# count = 0
# for i in range(1,30,2) :
#     print(i)
#     count += 1
#     if count == 10 :
#         break

# ##& Using while loop

# count = 0
# i = 1
# while i <= 30 :
#     print(i)
#     count += 1
#     if count == 10 :
#         break
#     i += 2

# i = 1
# count = 0
# while count < 10:
#     print(i)
#     i += 2
#     count += 1

# ##^=================================================================================================
# ##!=================================================================================================

# ##! ⚙️ 🟡 Medium Level – Loops with Conditions
# ##* 1.Find the factorial of a number using a for loop.
# ##* 2.Count digits in a number (e.g., 1234 → 4 digits).
# ##* 3.Reverse a number using a loop (e.g., 123 → 321).
# ##* 4.Check if a number is a palindrome (same forward and backward).
# ##* 5.Check whether a number is prime or not.
# ##* 6.Find the sum of digits of a number (e.g., 123 → 6).
# ##* 7.Display all prime numbers between 1 to 100.

# ##^=================================================================================================

# ##! 1.Find the factorial of a number using a for loop.

# ##& Using for loop.

# def fact(n) :
#     if n < 0 :
#         print("It is a negative number.")
#     elif n == 0 or n == 1 :
#         print(f"Factorial of {n} = 1")
#     else :
#         value = 1
#         for i in range(1,n+1) :
#             value *= i
#         print(f"Factorial of {n} = {value}")
# try :
#     n = int(input("Enter a number : "))
#     fact(n)
# except ValueError :
#     print("Number must be integer type.")

# ##& Using while loop.

# def fact(n) :
#     if n < 0 :
#         print("It is a negative number.")
#     elif n == 0 or n == 1 :
#         print(f"Factorial of {n} = 1")
#     else :
#         value = 1
#         i = 1
#         while i <= n :
#             value *= i
#             i+=1
#         print(f"Factorial of {n} = {value}")
# try :
#     n = int(input("Enter a number : "))
#     fact(n)
# except ValueError :
#     print("Number must be integer type.")

# ##^=================================================================================================

# ##! 2.Count digits in a number (e.g., 1234 → 4 digits).

# ##& Without loop

# number = input("Enter a number : ")
# if number.isdigit() :
#     count = len(number)
#     print(f"Digits in number {number} = {count}")
# else :
#     print("Add numbers only.")

# ##& Using for loop.
# def count(number) :
#     digit = str(number)
#     count = 0
#     for i in digit :
#         print(i,end='')
#         count += 1
#     print(f"\nDigits in a number {number} = {count}")
# try :
#     number = int(input("Enter a number : "))
#     count(number)
# except ValueError :
#     print("Number must be integer type only.")

# ##& Using while loop.
# def count(number) :
#     digit = str(number)
#     count = 0
#     i = 1
#     # while i <= len(digit) :
#     #     print(i,end='')
#     #     count += 1
#     #     i += 1
#     # print(f"\nDigits in a number {number} = {count}")
#     digit = str(number)
#     count = 0
#     i = 0
#     while i < len(digit):
#         print(digit[i], end='')
#         count += 1
#         i += 1
#     print(f"\nDigits in a number {number} = {count}")

# try :
#     number = int(input("Enter a number : "))
#     count(number)
# except ValueError :
#     print("Number must be integer type only.")

# ##^=================================================================================================

# ##! 3.Reverse a number using a loop (e.g., 123 → 321).

# ##& Without loops.

# t = input("Enter a number : ")
# if t.isdigit() :
#     p = ''.join(reversed(t))
#     print(f"Reversed number = {p}")
# else :
#     print("Enter numbers only.")

# ##& Using for loop.

# def rev(number) :
#     digit = str(number)
#     rev_num = ''
#     for i in range(len(digit)-1,-1,-1) :
#         rev_num += digit[i]
#     print(f"Reversed number = {rev_num}")
# try :
#     number = int(input("Enter a number : "))
#     rev(number)
# except ValueError :
#     print("Number must be Integer type.")

# ##& Using while loop.

# def rev(number) :
#     digit = str(number)
#     i = len(digit)-1
#     rev_num = ''
#     while i >= 0 :
#         rev_num += digit[i]
#         i -= 1
#     print(f"Reversed number = {rev_num}")
# try :
#     number = int(input("Enter a number : "))
#     rev(number)
# except ValueError :
#     print("Number must be Integer type.")

# ##^=================================================================================================

# ##! 4.Check if a number is a palindrome (same forward and backward).

# ##& Without loops.

# t = input("Enter a number : ").strip()
# if t.isdigit() :
#     p = ''.join(reversed(t))
#     if p == t :
#         print(f"{t} is a Palindrome number.")
#     else :
#         print(f"{t} is not a Palindrome number.")
# else :
#     print("Please enter numbers only.")

# ##& Using for loop.

# def palindrome(t) :
#     if t.isdigit() :
#         p = ''
#         for i in range(len(t)-1,-1,-1) :
#             p += t[i]
#         if p == t :
#             print(f"{t} is a Palindrome number.")
#         else :
#             print(f"{t} is not a Palindrome number.")
#     else :
#         print("Please enter numbers only.")

# t = input("Enter a number : ").strip()
# palindrome(t)

# ##& Using while loop.

# def palindrome(t) :
#     if t.isdigit() :
#         p = ''
#         i = len(t)-1
#         while i >= 0 :
#             p += t[i]
#             i -= 1
#         if p == t :
#             print(f"{t} is a Palindrome number.")
#         else :
#             print(f"{t} is not a Palindrome number.")
#     else :
#         print("Please enter numbers only.")

# t = input("Enter a number : ").strip()
# palindrome(t)

# ##^=================================================================================================

# ##! 5.Check whether a number is prime or not.

# ##& Using for loop.

# def prime(num):
#     if num == 0 or num == 1:
#         print(f"{num} is not a prime nor composite number.")
#     elif num < 0:
#         print("Negative numbers cannot be prime.")
#     else:
#         for i in range(2, num):
#             if num % i == 0:
#                 print(f"{num} is not a prime number.")
#                 break
#         else:
#             print(f"{num} is a prime number.")

# try:
#     num = int(input("Enter a number: "))
#     prime(num)
# except ValueError:
#     print("Number must be Integer type only.")

# ##& Using while loop.

# def prime(num):
#     if num == 0 or num == 1:
#         print(f"{num} is not a prime nor composite number.")
#     elif num < 0:
#         print("Negative numbers cannot be prime.")
#     else:
#         i = 2
#         while i < num:
#             if num % i == 0:
#                 print(f"{num} is not a prime number.")
#                 break
#             i += 1
#         else:
#             print(f"{num} is a prime number.")

# try:
#     num = int(input("Enter a number: "))
#     prime(num)
# except ValueError:
#     print("Number must be Integer type only.")

# ##^=================================================================================================

# ##! 6.Find the sum of digits of a number (e.g., 123 → 6).

# ##* abs() is a built-in function in Python that returns the absolute value 
# ##* of a number — that means:
# ##! 1.It removes the sign of the number.
# #! 2.The result is always non-negative.

# def sum_of_digits(num):
#     num = abs(num)  # handle negative numbers
#     s = 0
#     for digit in str(num):
#         s += int(digit)
#     print(s)

# ##& Using for loop.

# def sum(num) :
#     s = 0
#     dig = str(num)
#     for i in dig :
#         s += int(i)
#     print(s)
# try :
#     num = int(input("Enter a number : "))
#     sum(num)
# except ValueError :
#     print("Number must be integer type.")

# ##& Using while loop.

# def sum(num) :
#     s = 0
#     dig = str(num)
#     i = 0
#     while i <= len(dig)-1 :
#         s += int(dig[i])
#         i += 1
#     print(s)
# try :
#     num = int(input("Enter a number : "))
#     sum(num)
# except ValueError :
#     print("Number must be integer type.")
