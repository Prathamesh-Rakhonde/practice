
# ##!=================================================================================================
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

##! List

##& 1. list function help's us to store multiple types of data in a single object.
##& 2. To store multiple type of data we write it in [ ].
##& 3. list data is seprated by comma (,).

a = [1,1j,1.1,'parth']
print(a,type(a),id(a))

##& 4. List object is mutable means that list object id never change if we 
##&    cahnge something in original list or in its data.

a.append(1)
print(a,type(a),id(a))

##! ❌ Immutable Types
##? Objects cannot be changed after creation.
##? Example: int, float, str, tuple, bool

# ##^=================================================================================================

##! NOTE TO FUTURE ME : Remember this when working with lists inside functions or across variables!
# When working with lists, use list.copy(), list(), or slicing
# to make a true copy. Don't just assign with = if you don't want side effects!
# Copying a list: use .copy(), list(a), or slicing (a[:]) to create a new list.
# Don't just write `b = a`, because that only copies the reference — 
# changes to `b` will affect `a` too.

# ##^=================================================================================================