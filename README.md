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
age = 30
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
print(my_str[0:2]) #Sas
```
Apart from the **start** and **stop** indices, there's also an optional step parameter, which is used to specify the increment between each index in the slice
```
my_str = 'Sasi'
print(my_str[0:2:3]) #Ssi
```
A helpful trick you can do with the **step** parameter is to reverse a string by setting step to -1, and leaving start and stop blank:
```
my_str = 'Sasi'
print(my_str[::-1]) # Isas
```
### *What are some common string methods?**
Python provides a number of built-in methods to make easy working with strings.
```
my_str = 'sasi'
uppercase_my_str = my_str.upper()
print(uppercase_my_str) # SASI
```
```
my_str = 'SASI'
lowercase_my_str = my_str.lower()
print(lowercase_my_str) #sasi
```
**Strip()** returns a new string with the specified leading and trailing characters removed. If no argument is passed, it removes leading and trailing whitespace
```
my_str = '  sasi  '
trimmed_my_str = my_str.strip()
print(trimmed_my_str) # "sasi"
```
```
my_str = 'sasi'
replace_my_str = my_str.replace('sasi', 'kiran')
print(replace_my_str) #kiran
```
```
my_str = 'sasi kiran'
split_words = my_str.split()
print(split_words) # ['sasi', 'kiran']
```
**Join(iterable)** joins elements of an iterable into a string with a separator
```
my_list = ['sasi', 'kiran']
joined_my_str = ' '.join(my_list)
print(joined_my_str) # sasi kiran
```
```
my_str = 'sasi kiran'
starts_with_sasi = my_str.startswith(my_str)
print(starts_with_sasi) # True
```
```
my_str = 'sasi kiran'
ends_with_kiran = my_str.endswith(my_str)
print(ends_with_kiran) #True
```
**find(substring)** returns the index of the first occurence of the substring, or -1 if it doesn't find one
```
my_str = 'sasi kiran'
world_index = my_str.find('kiran')
print(world_index) #5
```
**count(substring)** returns the number of times a substring appears in a string
```
my_str = 'sasi kiran'
a_count = my_str.count('a')
print(a_count) # 2
```
**capitalize()** returns a new string with the first character capitalized and the other characters lowercased
```
my_str = 'sasi kiran'
capitalize_my_str = my_str.capitalize()
print(capitalize_my_str) #Sasi kiran
```
**isupper()** returns *true* if all letters in the string are uppercase and *false* if not
```
my_str = 'sasi kiran'
is_all_upper = my_str.isupper()
print(is_all_upper) # False
```
**islower()** returns *true* if all letters in the string are lowercase and *false* if not
```
my_str = 'sasi kiran'
is_all_lower = my_str.islower()
print(is_all_lower) # True
```
**title()** returns a new string with the first letter of each word capitalized
```
my_str = 'sasi kiran'
title_case_my_str = my_str.title()
print(title_case_my_str) # Sasi kiran
```
### *How do you work with integers and floating point numbers?*
Integers and floats are the primary numeric data types in Python. With them, you can store numeric data and perform mathematical operations. 

Integers are whole numbers without decimal points, either positive or negative
```
my_int_1 = 50
my_int_2 = 2

sum_ints = my_int_1 + my_int_2
print('Integer Addition:', sum_ints) # Integer Addition: 52

diff_ints = my_int_1 - my_int_2
print('Integer difference:', diff_ints) # Integer difference: 48

product_ints = my_int_1 * my_int_2
print('Integer product:', product_ints) # Integer product: 100

div_ints = my_int_1 / my_int_2
print('Integer Division:', div_ints) # Integer Division: 25

print(type(my_int_1)) # <class 'int'>
print(type(my_int_2)) # <class 'int'>
```

Floats are decimal numbers, either positive or negative
```
my_float_1 = 50.5
my_float_2 = 2.5

sum_floats = my_float_1 + my_float_2
print('Float addition:', sum_floats) # Float addition: 53

diff_floats = my_float_1 - my_float_2
print('Float difference:', diff_floats) # Float difference: 48

product_floats = my_float_1 * my_float_2
print('Float product:', product_floats) # Float product: 126.25

div_floats = my_float_1 / my_float_2
print('Float division:', div_floats) # Float division: 20.2

print(type(my_float_1)) # <class 'float'>
print(type(my_float_2)) # <class 'float'>
```
A modular operator **%** returns the reminder when the value on the left is divided by the value on right
```
my_int_1 = 50
my_int_2 = 2

mod_ints = my_int_1 % my_int_2
print('Integer modulus:', mod_ints) # Integer modulus: 0

my_float_1 = 50.5
my_float_2 = 2.5

mod_floats = my_float_1 % my_float_2
print('Float modulus:', mod_floats) # Float modulus: 20.2
```
**Floor Division (//)** divides two numbers and returns the greatest integer less than or equal to the result
```
my_int_1 = 50
my_int_2 = 4

floor_div_ints = my_int_1 // my_int_2
print('Integer floor division:', floor_div_ints) # Integer floor division: 12

my_float_1 = 50.2
my_float_2 = 4.4

floor_div_floats = my_float_1 // my_float_2
print('Float floor division:', floor_div_floats) # Float floor division: 11
```
**Exponentiation** raises a number to the power of another, and is done with **(**)
```
my_int_1 = 50
my_int_2 = 2

exp_ints = my_int_1 ** my_int_2
print('Integer exponentiation:', exp_ints) # Integer exponentiation: 2500

my_float_1 = 50.5
my_float_2 = 2.5

exp_floats = my_float_1 ** my_float_2
print('Float exponentiation:', exp_floats) # Float exponentiation: 18122.93
```
Python also provides built-in functions for converting either numeric data or strings into integers or floats.
```
my_int_1 = 50
my_float_1 = int(my_int_1)
print(my_float_1) # 50.0

my_float_1 = 50.5
my_int_1 = int(my_float_1)
print(my_int_1) #50

my_float_1 = 50.456
round_my_float = round(my_float_1)
print(round_my_float) #50.5

my_num = -3
abs_num = abs(my_num)
print(abs_num) #3

my_num = 50
binary_representation = bin(my_num)
print(binary_representation) #0b110010

my_num = 50
octal_representation = oct(my_num)
print(octal_representation) #0o62

my_num = 50
hexa_representation = hex(my_num)
print(hexa_representation) #0x32
```
**pow()** raises a number to the power of another or performs modular exponentiation
```
result_1 = pow(2,3)
print(result_1) # 8
```
### *How do augmented assignments work?**
Augmented assignment combines binary operation with an assignment in one step. It takes a variable, applies an operation to it with another value, and stores the result back into the same variable. The advantage of augmented assignment is that it provides a concise and readable way to update a variable value without repeating the variable name. In turn, it reduces redundancy and potential errors that might arise from a typo or something similar
```
count = 14
count -= 3
print(count) #11

product = 7
product *= 3
print(product) #21

price = 4
price /= 2
print(price) #2

total_pages = 24
total_pages //= 7
print(total_pages) #3

bits = 51
bits %= 2
print(bits) #1

power = 2
power **= 3
print(power) #8
```
You can use only addition and multiplication augmented assignments for strings. Other augmented assignments will throw **TypoError** during compilation
```
greet ='Hello'
greet += 'World'
print(greet) #Hello World

greet = 'Hi'
greet *= 3
print(greet) #HiHiHi
```
### *How do functions work in Python?*
Functions are reusable pieces of code that run when you call them. Python also come with some built-in functions like **print()**. Another helpful built-in function is **input()** which prompts the user for input
```
name = input('What is your name?') # User types Sasi and clicks ENTER
print('Hello', name) # Hello Sasi
```
To write own custom functions, you use the **def** keyword, followed by the name you want to give your function, a pair of parentheses and colon
```
def sasi_python():
```
In Python, code blocks are determined by indentation. Python style guide recommends using four spaces to determine each level of indentation
```
def calculate_sum(a, b):
    print(calculate_sum)
```
Here a, b which are represented in parantheses are called **Parameters**. To use the parameters, you have to pass in **Arguments**. Arguments are the values you pass to a function when you call it
```
calculate_sum(3, 5) #8
```
Functions also use special **return** keyword to exit the function and return a value. If you don't explicitly use it, Python will return **None** by default
```
def calculate_sum(a, b):
    print(a + b)

my_sum = calculate_sum(3, 5)
print(my_sum) #None

def calculate_sum(a, b):
    return a + b

my_sum = calculate_sum(3, 5)
print(my_sum) #8
```
### *What is scope in Python and how does it work?**
In Python, scope determines the point at which you can access a variable. It's what controls the lifetime of a variable and how it resolved in different parts of the code. To determine the scope, Python follows the **LEGB** rule:
1. **Local Scope (L)**: Variables defined in functions or classes
2. **Enclosing Scope (E)**: Variables defined in enclosing or nested functions
3. **Global Scope (G)**: Variables defined at the top level of the module or file
4. **Built-in Scope (B)**: Reserved names in Python for predefined functions, modules, keywords, and objects

**Local Scope** means that the variable declared inside a function or class can only be accessed within that function or class. In this case, my_func() has its own scope which cannot be accessed from outside the function 
```
def my_func()
  my_var = 3 # Locally scoped to my_func()
  print(my_var) #3
my_func #3
print(my_var) # NAME ERROR: name 'my_var' is not defined
```
**Enclosing Scope** means that a function that's nested inside another function can access the variables of the function it's nested within. The inner function can easily access the variable defined in the outer function. However, note that the outer functions cannot access variables defined within any nested functions
```
def outer_func():
    msg = 'Hi, Sasi!'
    res = "" # Declare res in the enclosing loop

    def inner_func():
        nonlocal res  # Allow modification in the enclosing variable
        res = 'How are you?'
        print(msg) # Accessing 'msg' from outer function

    inner_func()
    print(res) # Now res is accessible and modified

outer_func()
```
```
Output:
# Hi, Sasi!
# How are you?
```
**Global Scope** refers to variables that are declared outside any functions or classes which can be accessed from anywhere in the program. You can also use **global** keyword to modify a global variable
```
my_var_1 = 7

def show_vars():
    global my_var_2
    my_var_2 = 10
    print(my_var_1)
    print(my_var_2)

show_vars() # 7 10
```
### *How do conditional statements and logical operations work?*
Conditional statements or conditionals, let you control the flow of your program based on whether certain conditions are *true* or *false*. 
```
Equal (=)
Not Equal (!=)
Greater than (>)
Less than (<)
Greater than or equal to (>=)
Less than or equal to (<=)
```
In Python, the most basic conditional is the **if** statement.
1. If statements start with *if* keyword
2. Condition is an expression that evaluates to *True* or *False*, followed by colon
3. The indentation specifies the block of code within the body of *if* statement
```
if condition:
```
When you want to print something while *if* clause is not true, **else** clause comes into play. 
```
if condition:
else:
```
There might also be situations where you want to account for multiple conditions. To do that, Python lets you to extend you if statement with **elif** keyword
```
if condition1:
elif condition2:
else:
```
**Example**
```
age = 29

if age >= 65:
    print('You are a senior citizen')
elif age >= 30:
    print('You are an adult in your prime)
elif age >= 18:
    print('You are a young adult')
elif age >= 13:
    print('You are a teenager')
elif age >=3:
    print('You are a toddler')
else:
    print('You are a toddler or an infant')
```
```
Output:
# You are a young adult
```
### *What are Truthy and Falsy values, and how do Boolean operators and short-circuiting work?*
While conditional statements and comparison operators are very powerful, you will often run into situations where you need to compare multiple values at once. This can lead to nested conditional statements
```
is_citizen = True
age = 29

if is_citizen:
    if age >= 18
    print('You are eligible to vote')
else:
  print('You are not eligible to vote')
```
```
Output:
# You are eligible to vote
```
In Python, every value has an inherent boolean value, or a built-in sense of whether it should be treated as *True* or *False* in a logical context. Many values are considered **Truthy**, i.e., they evaluate to *True* in a logical context. Others are **Falsy**, i.e., they evaluate to *False*
```
Few falsy values:
1. None
2. False
3. Integer 0
4. Float 0.0
5. Empty Strings ""
```
Additionally, there are three Boolean operators in Python: **and**, **or**, **not**
```
is_citizen = True
age = 25

if is_citizen and age >= 18
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')

if is_citizen or age >= 18
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')
```
```
Output:
# You are eligible to vote
```
```
is_admin = False

if not is_admin:
    print('Access denied for non-administrators')
else:
    print('Welcome administrator!')
```
```
Output:
# Access denied for non-administrators
```
**isinstance()** function in Python is used to check if the object of an instance of a specified class or a tuple of classes. The all() and any() functions are used to evaluate iterables of boolean values. Combining these allows for powerful type checking with collectibles
```
data = [1, 2, 3, 4]
if all(isinstance(item, int) for item in data):
    return 'All elements are integers'

mixed_data = ['Sasi', 1, 0.8]
if not all(isinstance(item, int) for item in mixed_data):
    return 'Not all elements are integers'
```
```
mixed_list = ['Sasi', 1, 0.8]
if any(isinstance(item, str) for item in mixed_data):
    return 'There is at least one string in the list'

data = [10, 20, 30]
if not any(isinstance(item, str) for item in data:
    return 'There is no strings in the list'
```
----
## 🧒🏻 Loops & Sequences
### *What are lists and how do they work?*
The list data type is an ordered sequence of elements that can be compromised of strings, numbers, or even other lists. Lists are mutable and use zero-based indexing, meaning that the first element of the list is at index zero
To access an element from the list, you can reference its index number in the sequence
```
cities = ['Hyderabad', 'Mumbai', 'Bengaluru']
cities[0] # Hyderabad
```
Negative indexing is used to access elements from the end of the list instead of beginning at index **0**. To access the last element of any list, you can use **-1**
```
cities = ['Hyderabad', 'Mumbai', 'Bengaluru']
cities[-1] # Bengaluru
```
Another way to create a list is to use the **list()** constructor. It is used to convert an iterable into a list
```
consultant = 'Sasi'
list(consultant) #['S', 'a', 's', 'i']
```
An iterable is a special type of object that can be looped over one item at a time. 
To get the total number of elements in a list, you can use **len()** function
```
numbers = [1, 2, 3, 4, 5]
len(numbers) # 5
```
If you wanted to update a value at a particular index:
```
supply_chain_management = ['Supply Chain', 'Logistics', 'Manufacturing', 'Inventory']
supply_chain_management[0] = 'Warehousing'
print(supply_chain_management) # ['Warehousing', 'Logistics', 'Manufacturing', 'Inventory']
```
Since lists are mutable, you can update any element in the list as long as you pass in a valid index number. If you pass in an index (either positive or negative) that is out of bounds for the list, then you will receive an **IndexError**
If you want to remove an element from a list, you can use **del** keyword:
```
consultant = ['Sasi', 29, 'SCM consultant']
del consultant[1]
print(consultant) # ['Sasi', 'SCM consultant']
```
Sometimes it is helpful to check if an element is inside the list. To do that, you can use **in** keyword
```
supply_chain_management = ['Supply Chain', 'Logistics', 'Manufacturing', 'Inventory']
'Manufacturing' in supply_chain_management #True
'Marketing' in supply_chain_management #False
```
Sometimes it is common to have lists nested inside of other lists. To access the nested list, you need to access it using primary index followed by secondary index
```
consultant = ['Sasi', 29, ['Inventory Management', 'Digital Manufacturing', 'Lean Six Sigma management']]
developer[2][0] # Inventory Management
```
Unpacking values from a list is a technique used to assign values from a list to new variables. 
```
consultant = ['Sasi', 29, 'SCM Consultant']
name, age, job = consultant

print(name) #Sasi
print(age) #29
print(job) #SCM Consultant
```
If you need to collect any remaining elements from the list, you can use the asterisk **(*)** symbol
```
consultant = ['Sasi', 29, 'SCM Consultant']
name, *rest = consultant

print(name) #Sasi
print(rest) #[29, 'SCM Consultant]
```
Similar to strings, you can use slice operator **:** to access portions of a list
```
consultant[0:1] #['Sasi', 29]
```
### *What are the common methods used for lists?*
**append()** used to add an item to the end of the list.
```
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers) #[1, 2, 3, 4, 5, 6]

even_numbers = [8, 10, 12, 14]
numbers = append(even_numbers)
print(numbers) #[1, 2, 3, 4, 5, 6, [8, 10. 12, 14]]
```
**extend()** is similar to append() but you can add multiple items from one list to another
```
numbers = extend(even_numbers)
print(numbers) #[1, 2, 3, 4, 5, 6, 8, 10, 12, 14]
```
**insert()** accepts two arguments: the index where you wish to insert the new item and the item you want to insert
```
numbers.insert(2, 2.5)
print(numbers) # [1, 2, 2.5, 3, 4, 5, 6, 8, 10, 12, 14]
```
**remove()** will remove the duplicate number from the list
```
numbers.remove(3, 4, 5)
print(numbers) #[1, 2, 2.5, 6, 8, 10, 12, 14]
```
To remove an element at the specific index in the list, use **pop()** method
```
numbers.pop(2)
print(numbers) #[1, 2, 6, 8, 10, 12, 14]

numbers.pop()
print(numbers) #[1, 2, 6, 8, 10, 12]
```
**clean()** empties the list
```
numbers.clear()
print(numbers) #[]
```
**sort()** is used to sort elements in place
```
numbers = [19, 1, 7, 11, 25]
numbers.sort()

print(numbers) #[1, 7, 11, 19, 25]
```






