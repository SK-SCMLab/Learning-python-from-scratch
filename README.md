# 🐍 LEARNING PYTHON FROM SCRATCH
My personal knowledge hub — a GitHub-hosted notebook containing Python notes, experiments, cheat sheets, workflows, and topic-wise summaries. Organized cleanly, version-controlled, and updated as I learn new concepts

---

## 👶🏻 Introduction to Python
### *What is Python?*
Python is a general-purpose programming language known for its simplicity and ease of use. 
i. In web development, Python frameworks like Django, FastAPI, and Flask let developers build scalable and secure backend systems with minimal effort
ii. Cybersecurity professionals and ethical hackers use Python to detect vulnerabilities like malware and other viruses, build automated security scans, and analyze threats.
iii. Python runs well on microcomputers like the Raspberry Pi and MicroPython-compatible boards, so you can build all kinds of IoT projects like smart home devices, weather monitoring stations, and more
iv. Libraries like Selenium and BeautifulSoup also make it easy to interact with websites, so you can scrape public data, automate tasks through a web UI, and even manage cloud deployments for your projects
v. Libraries like Pandas and Numpy make data analysis less tedious, while others like Tensorflow and Scikit make machine learning and working with AI models much more accessible

### *How to install Python?*
https://www.python.org/

Follow the instructions as mentioned in the website

### *How to declare variables and what are the naming conventions to name variables?*
1. In Python, variables are like a labelled box for storing and referencing data of different types. To declare variables in Python, you need to assign a value to an identifier with the assignment **=** operator. You just need to write the name of the variable on the left, followed by the assignment operator, and the value you want to assign the variable on the right

```
name = 'Sasi'
age = '30'
```
2. When naming variables in Python, there are some important rules to keep in mind:
  i. Vairable names can only start with a letter or an underscore **_**, not a number
 ii. Variables names only contain alphanumeric characters (a-z, A-Z, 0-9) and underscores(_)
iii. Variable names are case-sensitive - age, Age, and AGE are all considered unique
 iv. Variable names cannot be one of Python's reserved keywords such as if, class, and def
If any of these rules are broken, Python program thows a **Syntax Error**:
3. In Python, comments start with a pound symbol **#**, and the language ignores everything while execution after the # on that line

```
# This is a single line comment
# This is a
# multi-line
# comment
```

### *How does the Print function work?*
Every programming language has some way to output data to the terminal with a built-in method, function, property, or keyword. In python, you can use **print** function to print data to the terminal. 

```
print('Hello', 'World!)
```
Python automatically adds a space between each item when you separate them with commas. This is helpful when you want to print several pieces of information together

### *What are the common data typs in Python and how do you get the type of a variable?*
Python is a dynamically-typed language, meaning you don't need to explicitly declare types for variables. The language knows what data type a variable is based on what you assign to it. The dynamic-typing nature of Python makes coding really fast and more flexible, but it can also lead to unexpected bugs because type errors are detected only when a program runs, not when the program complies. 
```
my_integer_var = 10
print('Integer:', my_integer_var)
```
```
my_float_var = 3.3
print('Float:', my_float_var)
```
```
my_complex_var = 3 + 1j
print('Complex:', my_complex_var)
```
```
my_string_var = 'Hi'
print('String:', my_string_var)
```
```
my_boolean_var = True
print('Boolean:', my_boolean_var)
```
```
my_set_var = {1, 2, 3}
print('Set:', my_set_var)
```
```
*Dictionary is a collection of key-value pairs enclosed in curly braces*
my_dictionary_var = {'name': 'Sasi', 'age': 29}
print('Dictionary:', my_dictionary_var)
```
```
*Tuple is an immutable ordered collection, enclosed in brackets
my_tuple_var = (1, 2, 3)
print('Tuple:', my_tuple_var)
```
```
*Range is a sequence of number, often used in loops
my_range_var = range(3)
print('Range:', my_range_var)
```
```
*List is an ordered collection of elements that supports different data types*
my_list = [29, 'Sasi', 3.3, True]
print(my_list)
```
```
*None is a special value that represents the absence of a value*
my_none_var = None
print('None:', my_none_var)
```

In Python, all data gets treated as objects and some objects are immuatable while others are mutable. Immutable data types can't be modified or altered once they're declared. For example: String, Integer, Float, Boolean, Tuple and Range. On the other hand, you can change mutable types without giving them a new name

```
nums = [1, 2, 3]
nums[0] = 5

print(nums) # [5, 2, 3]
```
To check the type of a variable is to use the built-in **isinstance()** function, which checks if a variable matches a specific data type. It takes in an object and the type you want to check it against, then returns a boolean

### *How do you work with strings?*
A string is a sequence of characters surrounded by either single or double quotation marks. In Python, they're treated equally.
```
my_str_1 = 'Sasi'
my_str_2 = "Sasi"
my_str_3 = """Sasi
SCM"""
my_str_4 = '''Sasi
SCM'''
```
Multiple strings can be combined using **+** operator. This process is called String Concatenation
```
str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Sasi Sasi
```
Note that this work only with strings. If you try to concatenate a string with a number, you'll get a **TypeError**
To fix this, you can convert the number into a string with the built-in str() function:
```
name = 'Sasi'
age = 29

name_and_age = name + str(age)
print(name_and_age) # Sasi29
```
You can also use augmented assignment operator for concatenation
```
name = 'Sasi'
age = 29

name_and_age = name
name_and_age += str(age)

print(name_and_age) #Sasi29
```

Apart from regular strings, Python also has a category of string called f-strings, which is short for formatted string literals. It allows you to handle interpolation and also do some concatenation with a compact and readable syntax. F-strings start with **f** (either lowercase or uppercase) before the quotes, and allow you to embed variables or expressions inside replacement fields indicated by {}
```
name = 'Sasi'
age = 29
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is Sasi and I am 29 years old
```
To get the length of a string, you can use built-in **len()** function
```
my_str = 'Sasi'
print(len(my_str)) # 4
```
Each character in a string has a position called an **Index**. The index is zero-based, meaning that the index of the first character of a string is 0, the index of the second character is 1 and so on. To access a character by its index, you use [] with the index of the character you want to access inside
```
my_str = 'Sasi'
print(my_str[0]) # S
```
Negative indexing is also allowed, so you can get the last/second-to-last character of any string
```
my_str = 'Sasi'
print(my_str[-1]) # i
```
**String Slicing** lets you extract a portion of a string or work with only a specific part of it
```
my_str = 'Sasi'
print(my_str[0:2] #Sas
```
Apart from the **start** and **stop** indices, there's also an optional step parameter, which is used to specify the increment between each index in the slice
```
my_str = 'Sasi'
print(my_str[0:2:3] #Ssi
```
A helpful trick you can do with the **step** parameter is to reverse a string by setting step to -1, and leaving start and stop blank:
```
my_str = 'Sasi'
print(my_str[::-1] # Isas
```
