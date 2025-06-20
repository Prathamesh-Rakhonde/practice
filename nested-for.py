
# # #! | Exception Name      | Cause                                         | Example                           |
# # #? | ------------------- | --------------------------------------------- | --------------------------------- |
# # #^ | `ZeroDivisionError` | Dividing a number by zero                     | `x = 5 / 0`                       |
# # #^ | `ValueError`        | Invalid value passed to a function            | `int("abc")`                      |
# # #^ | `TypeError`         | Unsupported operation or wrong data type      | `len(5)`                          |
# # #^ | `IndexError`        | Accessing invalid index in a list/tuple       | `lst = [1,2]; lst[5]`             |
# # #^ | `KeyError`          | Accessing a dictionary key that doesn't exist | `d = {'a':1}; d['b']`             |
# # #^ | `FileNotFoundError` | Trying to open a file that doesn’t exist      | `open('nofile.txt')`              |
# # #^ | `AttributeError`    | Accessing invalid attribute of an object      | `'hello'.append('!')`             |
# # #^ | `ImportError`       | Importing a module that doesn’t exist         | `import some_nonexistent_module`  |
# # #^ | `IndentationError`  | Incorrect indentation                         | Bad indentation in code           |
# # #^ | `NameError`         | Using a variable that hasn’t been defined     | `print(x)` where `x` is undefined |

# # ##!=================================================================================================

# ##! 🟢 Easy Level

# ## 1.Print a Square of Stars

# # ****
# # ****
# # ****
# # ****
# # ➤ Write a nested loop to print a 4x4 grid of *.

# ## 2.Print a Right-Angled Triangle
# # *
# # **
# # ***
# # ****
# # ➤ Use nested loops to print a triangle pattern.

# ## 3.Print Numbers in a Grid
# # 1 2 3
# # 1 2 3
# # 1 2 3
# # ➤ Print numbers from 1 to 3 in 3 rows.

# ## 4.Print Multiplication Table (1–5)
# # ➤ Print a 5x5 multiplication table using nested loops.

# ## 5.Print this pattern.
# # ****
# # ***
# # **
# # *
# # ➤ Use nested loops to print a triangle pattern.

# ## 6. Print this pattern
## 1
## 1 2
## 1 2 3
## 1 2 3 4
## 1 2 3 4 5

# ## 7. Print this pattern
## 5 4 3 2 1
## 4 3 2 1
## 3 2 1
## 2 1
## 1

# ##^=================================================================================================

# ##& 1.Print a Square of Stars

# ## ****
# ## ****
# ## ****
# ## ****
# ##! ➤ Write a nested loop to print a 4x4 grid of *.

# ##^ Without nested loop just a single loop.

# for i in range(1,5) :
#     print('* '*4)

# i = 1
# while i <= 4 :
#     print('* '*4)
#     i += 1

# ##^ Using for in for method.

# for i in range(1,5) :
#     for j in range(1,5) :
#         print("*",end=" ")
#     print()

# r = 4
# for i in range(1,r+1) :
#     for j in range(1,r+1) :
#         print('*',end=' ')
#     print()

# ##^ Using while in for method.

# r = 4
# for i in range(1,r+1) :
#     j = 1
#     while j <= r :
#         print('*',end=' ')
#         j+=1
#     print()

# ##^ Using for in while method.

# r = 4
# j = 1
# while j <= r :
#     for i in range(1,r+1) :
#         print("*",end=' ')
#     j += 1
#     print()

# ##^ Using while in while method.

# r = 4
# i = 1
# while i <= r :
#     j = 1
#     while j <= r :
#         print('*',end=' ')
#         j += 1
#     i += 1
#     print()

# ##^=================================================================================================

# ##& 2.Print a Right-Angled Triangle

# ## *
# ## **
# ## ***
# ## ****
# ##! ➤ Use nested loops to print a triangle pattern.

# ##^ Without nested loop.

# for i in range(1,5) :
#     print('* '*i)

# i = 1
# while i <= 4 :
#     print('* '*i)
#     i += 1

# ##^ Using for in for method.

# for i in range(1,5) :
#     for j in range(1,i+1) :
#         print('*',end=" ")
#     print()

# ##^ Using while in for method.

# for i in range(1,5) :
#     j = 1
#     while j <= i :
#         print("*",end=' ')
#         j+=1
#     print()
        
# ##^ Using for in while method.

# i = 1
# while i <= 4 :
#     for j in range(1,i+1) :
#         print("*",end=" ")
#     i += 1
#     print()

# ##^ Using while in while method.

# i = 1
# while i <= 4 :
#     j = 1
#     while j <= i :
#         print("*",end=" ")
#         j += 1
#     i += 1
#     print()

# ##^=================================================================================================

# ##& 3.Print Numbers in a Grid

# ##* 1 2 3
# ##* 1 2 3
# ##* 1 2 3
# ##! ➤ Print numbers from 1 to 3 in 3 rows.

# ##^ Without nested loops.
# ##& Not good logic but okey for practicing.

# p = '1 2 3'
# for i in range(1,4) :
#     print(p)

# ##^ Using for in for method.

# for i in range(1,4) :
#     for j in range(1,4) :
#         print(j,end=" ")
#     print()

# ##^ Using while in for.

# for i in range(1,4) :
#     j = 1
#     while j <= 3 :
#         print(j,end=' ')
#         j+=1
#     print()

# ##^ Using for in while.

# i = 1
# while i <= 3 :
#     for j in range(1,4) :
#         print(j,end=' ')
#     i += 1
#     print()

# ##^ Using while in while.

# i = 1
# while i <= 3 :
#     j = 1
#     while j <= 3 :
#         print(j,end=' ')
#         j += 1
#     i += 1
#     print()

# ##^=================================================================================================

# ##& 4.Print Multiplication Table (1–5)
# ##! ➤ Print a 5x5 multiplication table using nested loops.

# ##^ Using for in for loop

# # for i in range(1,6) :
# #     for j in range(1,6) :
# #         print(i*j,end=' ')
# #     print()

# ##^ Using while in for method.

# # for i in range(1,6) :
# #     j = 1
# #     while j <= 5 :
# #         print(i*j,end=' ')
# #         j += 1
# #     print()

# ##^ Using for in while method.

# # i = 1
# # while i <= 5 :
# #     for j in range(1,6) :
# #         print(i*j,end=' ')
# #     i += 1
# #     print()

# ##^ Using while in while.

# i = 1
# while i <= 5 :
#     j = 1
#     while j <= 5 :
#         print(i*j,end=' ')
#         j += 1
#     i += 1
#     print()

##^=================================================================================================

# ##& 5.Print

# ## ****
# ## ***
# ## **
# ## *
# ##!➤ Use nested loops to print a triangle pattern.

# ##^ Using for in for method.

# # for i in range(4,0,-1) :
# #     for j in range(i) :
# #         print("*",end=' ')
# #     print()

# ##^ Using while in for method.

# # for i in range(4,0,-1) :
# #     j = 1
# #     while j <= i :
# #         print("*",end=' ')
# #         j += 1
# #     print()

# ##^ Using for in while method.

# # i = 4
# # while i >= 1 :
# #     for j in range(i) :
# #         print('*',end=' ')
# #     i -= 1
# #     print()

# ##^ Using while in while method.

# # i = 4
# # while i >= 1 :
# #     j = i
# #     while j >= 1 :
# #         print("*",end=' ')
# #         j -= 1
# #     i -= 1
# #     print()

# ##^=================================================================================================

# ##& 6. Print this pattern
# ##* 1
# ##* 1 2
# ##* 1 2 3
# ##* 1 2 3 4
# ##* 1 2 3 4 5

# ##^ Using for in for method

# for i in range(1,6) :
#     for j in range(1,i+1) :
#         print(j,end=' ')
#     print()

# ##^ Using while in for method.

# # for i in range(1,6) :
# #     j = 1
# #     while j <= i :
# #         print(j,end=' ')
# #         j += 1
# #     print()

# ##^ Using for in while method.

# # i = 1
# # while i <= 5 :
# #     for j in range(1,i+1) :
# #         print(j,end=' ')
# #     i += 1
# #     print()

# ##^ Using while in while method.

# # i = 1
# # while i <= 5 :
# #     j = 1
# #     while j <= i :
# #         print(j,end=' ')
# #         j += 1
# #     i += 1
# #     print()

# ##^=================================================================================================

# ##& 7. Print this pattern

# ##* 5 4 3 2 1
# ##* 4 3 2 1
# ##* 3 2 1
# ##* 2 1
# ##* 1

# ##^ Using for in for method.

# # for i in range(5,0,-1) :
# #     for j in range(i,0,-1) :
# #         print(j,end=' ')
# #     print()

# ##^ Using while in for method.

# # for i in range(5,0,-1) :
# #     j = i
# #     while j >= 1 :
# #         print(j,end=' ')
# #         j -= 1
# #     print()

# ##^ Using for in while method.

# # i = 5
# # while i >= 1 :
# #     for j in range(i,0,-1) :
# #         print(j,end=' ')
# #     i -= 1
# #     print()

# ##^ Using while in while method.

# # i = 5
# # while i >= 1 :
# #     j = i
# #     while j >= 1 :
# #         print(j,end=' ')
# #         j -= 1
# #     i -= 1
# #     print()

##^=================================================================================================
##!=================================================================================================

##! 🟡 Medium Level

##& Print a Pyramid Pattern

#    *
#   * *  
#  * * * 
# * * * *
##! ➤ Use nested loops to create a centered pyramid of *.



##^=================================================================================================

##& Create a Chessboard Pattern

##* # # # #
##* # # # #
##* # # # #
##* # # # #
##! ➤ Use nested loops to alternate symbols like a checkerboard.

# List All Pairs in Two Lists
# list1 = [1, 2]
# list2 = ['a', 'b']
# ➤ Output:
# (1, 'a')
# (1, 'b')
# (2, 'a')
# (2, 'b')

# Print Diagonal Pattern
# *      
#   *    
#     *  
#       *
# ➤ Print a diagonal of * across a square.

##^=================================================================================================

##^=================================================================================================
##!=================================================================================================

# 🔴 Hard Level

# Spiral Number Pattern
# ➤ Create a spiral matrix like:
# 1  2  3
# 8  9  4
# 7  6  5

# Pascal's Triangle
# ➤ Generate Pascal's triangle using nested loops:
#     1
#    1 1
#   1 2 1
#  1 3 3 1

# Diamond Pattern
#    *
#   ***
#  *****
#   ***
#    *

# Matrix Transposition
# ➤ Given a 2D list (matrix), print its transpose using nested loops.

##^=================================================================================================

##^=================================================================================================
##!=================================================================================================