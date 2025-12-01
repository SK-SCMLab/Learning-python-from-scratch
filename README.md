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
