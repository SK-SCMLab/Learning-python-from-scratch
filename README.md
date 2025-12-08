# 🐍 LEARNING PYTHON FROM SCRATCH
My personal knowledge hub — a GitHub-hosted notebook containing Python notes, experiments, workflows, and topic-wise summaries. Organized cleanly, version-controlled, and updated as I learn new concepts

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
In contrast to sort() method, there is **sorted()** function which works for any iterable and returns a new sorted list instead of modifying the original list
```
numbers = [19, 1, 7, 11, 25]
sorted_numbers = sorted(numbers)

print(numbers) # [19, 1, 7, 11, 25]
print(sorted_numbers) # [1, 7, 11, 19, 25]
```
**reverse()** method will reverse a list of elements
```
numbers = [6, 5, 4, 3, 2, 1]
numbers.reverse()
print(numbers) #[1, 2, 3, 4, 5, 6]
```
**index()** is used to find the first index where an element can be found in a list. If the specified item within index() function cannot be found, then Python raises a **ValueError**
```
consultant = ['Sasi', 29, 'SCM Consultant']
consultant.index('SCM Consultant') # 2
```
### *What are tuples and how do they work?**
A tuple is a Python data type used to create a ordered sequence of values. Tuples can contain a mixed set of data types
```
consultant = ('Sasi', 29, 'SCM Consultant')
```
Tuples are similar to lists, but while lists are a mutable data type, tuples are immutable. This means that the elements in a tuple cannot be changed once it's created. If you try to update/delete one of the items in the tuple, you will get a **TypeError**
### *What are some common methods for Tuples?*
**count()** is used to determine how many times an item appears in a tuple. Arguments are expected to be passed into the count() method. If the specified item is count() function is not present at all in the tuple, then the return value is 0. If no arguments are passed into the count(), then Python raises a **TypeError**
```
consultant = ['Sasi', 29, 'SCM Consultant']
consultant.count('Sasi') #1
consultant.count('engineer') # 0
```
Similary index(), sorted(), reverse() methods can also be used on tuples
### *How do loops work?*
**for** loop is used to iterate through a list and print each item to the console. It can also used to iterate through other iterables like a string. **for** loops can also be nested
```
experience = ['Capgemini', 'ITC Infotech', 'Reliance Retail', 'AIG']
qualifications = ['B.Tech', 'MBA']

for exp in experience:
  for eligibility in qualifications:
    print(exp, eligibility)
```
In the above example, the outer loop will iterate through each exp in the experience list. For each exp, the inner loop will iterate through each eligibility in the qualifications

**while** loop will repeat a block of code until the code is False. 
```
secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input('Guess the number (1-5))
    if guess != secret_number:
        print('Wrong! Try again')

print('You got it!')
```
In the above example, we have a *secret_number* variable with the value of 3 and an initial guess of 0. Then we use the input function to get input from the user, then convert the input string into and integer with the int() function, and assign it to the guess variable. If the user guesses correctly by inputting 3, the while loop is broken out of and the message 'You got it!' is printed to the console. Otherwise, the message 'Wrong! Try again' is printed in the console, and the loop repeats.

The **break** statement is used to stop the execution of a loop
```
consultant_names = ['AB', 'CD', 'EF', 'GH']

for consultant in consultant_names:
    if consultant == 'EF':
        break
    print(consultant)
```
In the example, we iterate through a list of consultant_names and print each name to the console. If the name is equal to 'EF', then we break out of the loop. This results in only the names ['AB', 'CD'] being printed to the console

The **continue** statement is used to skip the current iteration of a loop and move onto the next iteration
```
consultant_names = ['AB', 'CD', 'EF', 'GH']

for consultant in consultant_names:
    if consultant == 'EF':
        continue
    print(consultant)
```
Now the result in the console will be different. The names ['AB', 'CD', 'GH'] are printed because the continue statement skips the second iteration of the loop when consultant name is equal to 'EF', and does not print that name to the console
Both *for* and *while* loops can be combined with an *else* clause, which is executed only when the loop is not terminated by a *break* statement
```
courses = ['Logistics', 'Operations', 'Marketing', 'Finance', 'Accounting']

for course in courses:
    for letter in course:
      if letter.lower() in 'aeiou':
      print(f"'{course}' contains the vowel '{letter'}")
      break
    else:
        print(f"'{course}' has no vowels")
```
### *What are ranges and how can you use them in the loops?*
The **range()** function is used to generate a sequence of integers. The *start* argument represents the start of the range, if not specified, the default is 0. The required *stop* argument is an integer that represents the end point for the sequence of numbers being generated. By default, the sequence of integers will increment by 1. But if you want to change that default, then you can use the optional *step* argument. Range() function only accepts integers as arguments, not floats. 
```
for num in range(1, 10, 2):
  print(num) # [1, 3, 5, 7, 9]
```
Alternatively, range() function can create a list of integers by using it with the list() constructor. It is used to convert the iterable into a list
```
numbers = list(range(1, 10, 2)
print(numbers) #[1, 3, 5, 7, 9]
```
### *What are the enumerate and zip functions and how do they work?*
To keep track of the index for each element: one option is to create an index variable and increment it by 1 for each iteration of the loop
```
courses = ['Logistics', 'Operations', 'Marketing', 'Finance', 'Accounting']
index = 0
for course in courses:
    print(f'Index {index} and course{courses}')
    index += 1
```
While that works, an even easier way to do that is by using **enumerate()** function. This function keeps track of the index for an iterable and returns an enumerate object
```
courses = ['Logistics', 'Operations', 'Marketing', 'Finance', 'Accounting']
for index, course in enumerate(courses):
    print(f'Index {index} and course{course})
```
**Output**
```
Index 0 and course Logistics
Index 1 and course Operations
Index 2 and course Marketing
Index 3 and course Finance
Index 4 and course Accounting
```
This function also accepts an optional *start* argument that specifies the starting value for the count. If this argument is omitted, then the count will begin at 0. It is used to iterate over one list
```
courses = ['Logistics', 'Operations', 'Marketing', 'Finance', 'Accounting']
for index, course in enumerate(courses, 1):
    print(f'Index{index} and course{course})
```
**Output**
```
Index 1 and course Operations
Index 2 and course Marketing
Index 3 and course Finance
Index 4 and course Accounting
```
**zip()** function which combines lists into paris of elements and returns an iterator of tuples is used to iterate over multiple iterables in parallel
```
courses = ['Logistics', 'Operations', 'Marketing', 'Finance', 'Accounting']
ids = [1, 2, 3, 4, 5]
list(zip(course, ids)) #[('Logistics', 1), ('Operations', 2), ('Marketing', 3), ('Finance', 4), ('Accounting', 5)]

for name, id in zip(courses, ids):
    print(f'Name:{name})
    print(f'ID:{id}')
```
**Output**
```
Name: Logistics
ID: 1
Name: Operations
ID: 2
Name: Marketing
ID: 3
Name: Finance
ID: 4
Name: Accounting
ID: 5
```
The enumerate() and zip() functions are very powerful, and when combined with loops, can make your code much more concise
### *What are list competencies and what are some useful functions to work with Lists?*
```
even_numbers = []
for num in range(21):
    if num % 2 == 0:
       even_numbers.append()
print(even_numbers)
```
For the above code, there is a more concise way to write that uses list comprehension instead. List comprehension allows you to create a new list in a single line by combining a loop and condition directly within square brackets. This makes code shorter and often easier to read
```
even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)
```
```
numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result) # [(1, 'Odd'), (2, 'Even'), (3, 'Odd'), (4, 'Even'), (5, 'Odd')]
```
Another way to create a list starting from an existing iterable is **filter()** function. It is used to select elements from an iterable that meet a specific condition. It accepts a function and an iterable for its arguments
```
words = ['green', 'blue', 'brown', 'olive green', 'white', 'yellow']

def is_long_word(word):
      return len(word) > 5

long_words = list(filter(is_long_word, words))
print(long_words) #['olive green', 'yellow']
```
Similarly **map()** function takes an iterable and applies a function to each of its elements
```
celsius = [0, 10, 20, 30, 40]
def to_fahrenheit(temp):
    return (temp * 9/5) + 32
fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit) #[32.0, 50.0, 68.0, 86.0, 104.0]
```
**sum()** function is also used to get the sum from an iterable like a list or tuple
```
numbers = [3, 2, 1, 0]
total = sum(numbers)
print(total) #6
```
### *What are Lamda functions and how do they work?*
Lambda functions are anonymous and are great when you need to use them in higher order functions. Both regular functions and lambda functions have their use cases in Python. If you are dealing with single inline expressions, then you might consider using a lambda function
```
def square(num):
    return num ** 2
print(square(4)) # 16
--------------------------
lambda num: num ** 2
--------------------------
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
```
## 🧑🏻 Dictionaries and sets
### *What are dictionaries and how do they work?*
In Python, dictionaries are built-in data structures that store collections of key-value pairs. They work very similarly to real dictionaries, where you search for a word to find its corresponding meaning. With Python dictionaries, you can use a key to find its corresponding value. You should use dictionaries when you need to associate values to unique keys. This is helpful when you need to find a value fast based on the key, and when you need to represent structured data. First, we find the variable that holds the dictionary. You don't necessarily need to assign the dictionary to a variable, but it's very common to do this to keep it in a memory and use it later in the code. Then that's followed by curly braces, containing key-value pairs. Each key is associated with a value, so you can use the key to access that value. After each value, except the last one, there's a comma to separate different key-value pairs. Keys must be unique in the dictionary, and they must be an immutable data type. However, the values can be repeated, and they can be of any data type
```
pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}
```
Alternatively, **dict()** constructor can be used which builds the dictionary from a sequence of key-value pairs. We pass a list of tuples as argument to the dict() constructor. These tuples contain the key as the first element and the value as the second element
```
pizza = dict([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])
```
Dictionaries also have helpful methods to perform common operations. The **.get()** method retrieves the value associated with a key. It's similar to the bracket notation that we just used, but it's advantage is that you can set a default value, so you won't get an error if the key doesn't exist.
```
pizza.get('toppings', []) #['mozzarella', 'basil']
```
The **.keys()** and **.values()** methods return a view object with all the keys and values in the dictionary, respectively:
```
pizza.keys()
#dict_keys(['name', 'price', 'calories_per_slice'])

pizza.values()
#dict_values(['Margherita Pizza', 8.9, 250])
```
The **.items()** method returns a view object with all the key-value pairs in the dictionary, including both the keys and the values:
```
pizza.items()
#dict_items([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250)])
```
The **.clear()** method removes all the key-value pairs from the dictionary
```
pizza.clear()
```
The **.pop()** method removes the key-value pair with the key that you specify as the first argument and return its value. If the key doesn't exist, it returns the default value that you specify as the second argument. If the key doesn't exist and you don't pass a default value, a **KeyError** is raised
In recent Python versions, **.popitem()** method removes the last inserted item
```
pizza.pop('price', 10)
pizza.popitem()
```
The **.update()** method updates the key-value pairs with the key-value pairs of another dictionary. If they have keys in common, their values are overwritten
```
pizza.update({'price': 15, 'total_time': 25})
pizza = {
          'name': 'Margherita Pizza',
          'price': 15,
          'calories_per_slice': 250,
          'toppings': ['mozzarella', 'basil']
          'total_time': 25
        }
```
### *What are the common techniques to loop over a dictionary?*
You can loop over a dictionary if you need to access and process its key-value pairs. This is helpful for updating their values or applying some logic to them
```
products = {
      'Laptop': 990,
      'Smartphone': 600,
      'Tablet': 250,
      'Headphones': 70,
}
```
The .values(), .keys(), .items() methods are essential for these techniques. You can use these view objects in **for** loops to iterate over the elements
```
for price in products.values():
  print(price)
# 990 600 250 70

for product in products.keys():
  print(product)
# Laptop smartphone Tablet Headphones

for product in products.items():
  print(product)
# ('Laptop', 990) ('Smartphone', 600) ('Tablet', 250) ('Headphones', 70)

for product, price in products.items():
  print(product, price)
# Laptop 990 Smartphone 600 Tablet 250 Headphones 70
```
For example, if we want to offer a 20% discount across all the products, we would multiple each prices by 0.8 and reassign it as the value of that product key
```
products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}
for product, price in products.items():
    products[product] = round(price * 0.8)
print(products)
```
**Output**
```
{
  'Laptop': 792,
  'Smartphone': 480,
  'Tablet': 200,
  'Headphones': 56
}
```
If you need to iterate over the key-value pairs while keeping track of a counter, you can call the enumerate() function. This counter essentially acts as a sort of "index" or "count" for that element within the loop. But enumerate() function also assigns an integer to each key, so we get tuples with the integer and the key
```
for product in enumerate(products):
    print(product)
```
**Output**
```
(0, 'Laptop')
(1, 'Smartphone')
(2, 'Tablet')
(3, 'Headphones')
```
You can also use loop variables to determine the index value
```
for index, price in enumerate(products.values()):
    print(index, price)
```
**Output**
```
0 990
1 600
2 250
3 70
```
### *What are sets, and how do they work?*
Sets are one of Python's built-in data structures. One of the core characteristics of sets is that they don't store duplicate values. Sets are mutable and unordered, which means that their elements are not stored in any specific order, so you cannot use indices or keys to access them. They can only contain values of immutable data types like numbers, strings, and tuples. And they support mathematical set operations, including union, intersection, difference, and symmetric difference. To define an empty set, you must use the **set()** function. 
```
my_set = {1, 2, 3, 4, 5}
my_set = set([1, 2, 3, 4, 5, 6])
```
Methods such as:
- .add(): pass the new element as argument
- .remove(): pass in the element that you want to remove as argument. It will raise **KeyError** if the element is not found
- .discard(): pass in the element that you want to remove as argument. It will not raise **KeyError** if the element is not found
- .clear(): removes all the elements from the set
- .issubset() & .issuperset(): check if a set is a subset or superset of another set, respectively
- .isdisjoint(): checks if two sets are disjoint, which means they don't have any elements in common
```
my_set.add(6) # {1, 2, 3, 4, 5, 6}
my_set.remove(4) #{1, 2, 3, 5, 6}
my_set.discard(7) #
my_set.clear() #{}

my_set = {1, 2, 3, 4, 5, 6, 7}
your_set = {3, 4, 5}
print(your_set.issubset(my_set)) # False
print(my_set.issuperset(your_set)) # True
print(my_set.isdisjoint(your_set)) # False
```
Operators such as:
- Union (|): returns a new set with all the elements from both sets
- Intersection (&): returns a new set with only the elements that the sets have in common
- Difference (-): returns a new set with the elements of the first set that are not in the other sets
- Symmetric difference (^): returns a new set with the elements that are either on the first or the second set, but not both
```
my_set = {1, 2, 3, 4, 5, 6}
your_set = {4, 5, 6, 7}
my_set | your_set #{1, 2, 3, 4, 5, 6, 7}
my_set & your_set # {4, 5, 6}
my_set - your_set #{1, 2, 3}
my_set ^ your_set #{1, 2, 3, 7}
```
### *What is the Python Standard Library, and how do you import a module?*
In software development, a library is like a toolbox for developers. Python has an extensive standard library with many difficult built-in modules. They're all standardized, well-vetted solutions for many of the problems and tasks you'll face daily as a programmer, such as:
- Interacting with the operating system
- Working with files
- Networking
- Working with date & time
- Performing mathematical operations
- Using regular expressions
- Testing and debugging your code
- Etc.
Modules such as:
- math(): Helpful for functions for performing more complex mathematical operations
- random(): helpful for generating random numbers
- re(): used for working with regular expressions
- datetime(): helpful for working with dates and times
**import()** statement let you import modules into your Python script. Import statements work exactly the same for functions, classes, constants, variables, and any other elements defined in the module
**as** is used to import the module with a different name
**__name__** is a special built-in variable in Python. When the Python file is executed directly, it sets the value of this variable to the string "__main__". It contains the code that you want to run only if the Python script is running as the main program
```
if __name__ == '__main__':
    #code
```
But if the script is imported as a module, the code with in the block doesn't run. It serves two purposes: They can be run directly to execute their main logic, or they can be imported into another module without executing their main logic

## 👦🏻 Understanding Error Handling
### *What are some common error messages in Python?*
When writing Python code, it's common to run into errors. Understanding these errors is key to debugging your code quickly and efficiently. These messages tell you exactly what went wrong, if you know how to read them. Common Python errors include *SyntaxError, NameError, TypeError, IndexError, and AttributeError*. These occur when Python doesn't understand your code, or when your logic doesn't match the data you're working with.
```
print("Hello, world!"
# SyntaxError: unexpected EOF while parsing

print(name)
# NameError: name 'name' is not defined

5 + "5"
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

my_list = [1, 2, 3]
print(my_list[5])
# IndexError: list index out of range

num = 42
num.append(5)
# AttributeError: 'int' object has no attribute 'append'
```
Recognizing common Python error messages helps you fix problems faster. Instead of guessing, read the error message carefully, it often tells you exactly what when wrong and where to look

### *What are some good debugging techniques in Python?*
Debugging is an essential skills for any Python developer. Understanding foundational techniques can help you identify and fix issues efficiently. Debugging is the process of identifying and resolving errors or bugs in your code. It involves examining the code, understanding the flow, and using tools to pinpoint the source of problems
First, using the **print()** function and f-strings at various points in your code can help you understand the flow and state of variables. F
```
def add(a, b):
    result = a + b
    print(f'Adding {a} and {b} gives {result}')
    return result
```
Next, you can utilize Python's built-in **pdb** module for interactive debugging: 
```
import pdb
def divide(a, b):
    pdb.set_trace()
    return a / b

print(divide(10, 2))
```
By setting the trace with **.set_trace()** method, you can step through the code, inspect variables, and understand the program's behavior
If you want to look at the type of elements throughout your code at that moment, you can use the **whatis** command
```
(Pdb) whatis a
<class 'int'>
(Pdb) whatis divide
Function divide
```
Many Integrated Development Environments (IDEs) offer advanced debugging tools, such as breakpoints, step execution, and variable inspection
#### Using VS Code Debugger
If you use VS code, you can set breakpoints in your code and run the debugger to pause execution at those points. 
**Step 1**: Set up your code => Create a file called main.py with the following content
```
def divide(a, b):
    result = a / b
    return result
print(divide(10, 2))
print(divide(15, 3))
```
**Step 2**: Set a breakpoint
1. Click in the gutter (left margin) next to line 2 (result = a / b) to set a breakpoint
2. A red dot will appear, indicating the breakpoint is set

**Step 3**: Start debugging
1. Press **F5** or go to Run > Start Debugging
2. Select "Python File" when prompted
3. The debugger will pause execution at your breakpoint

**Step 4**: Inspect variables
- Hover over variables to see their current values
- Use the variables panel on the left to see all local variables
- Use the Debug Console at the bottom to evaluate expressions

**Step 5**: Step through code
  Use the debug toolbar to:
  - **Continue(F5)**: Resume execution until the next breakpoint
  - **Step Over (F10)**: Execute the current line and move to the next
  - **Step Into (F11)**: Enter into function calls
  - **Step Out(Shift+F11)**: Exit the current function
IDE debugging tools provide a visual interface to examine the state of your program, making it easier to identify and fix issues compared to using print statements alone
print() statements for quick checks, pdb for interactive exploration, and IDE debuggers for visual inspection

### *How does exception handling work?*
In Python, exception handling is a core part of writing robust and fault-tolerant programs. It allows you to anticipate, catch, and respond to errors in a structured way. Exception handling is the process of catching and managing errors that occur during the execution of a program, so your  code does't crash unexpectedly. Python provides the **try, except, else, and finally** blocks to gracefully handle errors.
```
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!"
```
**try** block of code where your anticipate an error might occur
**except** runs if an error of the specified type is raised inside the try
In this case, dividing by zero raises a **ZeroDivisionError**, which is then caught and handled
```
try:
    x = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print('Division successful:', x)
finally:
    print('This block always runs.')
```
**else** runs if no exception is raised in the try block
**finally** runs no matter what - whether or not exception occurred. Useful for clean-up tasks like closing files or releasiong resource
```
try:
    number = int('abc')
    result = 10 / number
except ValueError:
    print('That was not a valid number.')
except ZeroDivisionError:
    print("Can't divide by zero.")
```
By using separate **except** clauses, you can make your error responses more specific and useful. You can also use the exception object, which is typically aliased to another name with the **as** keyword
```
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f'Error occurred: {e}')
```
### *What is the Raise statement and how does it work?*
In Python, the **raise** statement is a powerful tool that allows you to manually trigger exceptions in your code. It gives you control over when an how errors are generated, enabling you to create custom error conditions and enforce specific program behavior. The **raise** statement is used to explicitly throw an exception at any point in your program, allowing you to signal that error condition has occurred or that certain requirements haven't been met. 
```
def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    return age

try:
    check_age(-5)
except ValueError as e:
    print(f'Error: {e}') # Error: Age cannot be negative
```
This statement (without arguments) can also be used to re-raise the current exception, which is particularly useful in exception handling
```
def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError:
          print('Logging: Invalid data received')
          raise # Re-raises the same ValueError
try:
    process_data('abc')
except ValueError:
    print('Handled at higher level')
```
It allows you to log or perform cleanup while still propagating the error up the call stack
```
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f'Insufficient funds: ${balance} available, ${amount} requested')

def withdraw(balance, amount):
    if amount > balance:
        raise > InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f'Transaction failed: {e}')
```
It can also be used with the **from** keyword to chain exceptions, showing the relationship between different errors
```
def parse_config(filename):
    try:
        with open(filename, 'r') as file:
              data = file.read()
              return int(data)
    except FileNotFoundError:
      raise ValueError('Configuration file is missing') from None
    except ValueError as e:
      raise ValueError('Invalid configuration format') from e
config = parse_config('config.txt')
```



