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
