# Python Practice Exercises with Solutions
# Suitable for Jupyter Notebook or Python Script
# Author: Auto-generated for GitHub Repository

# --------------------
# Section 1: Basics
# --------------------

# Exercise 1: Print Hello World
print("Hello, World!")

# Exercise 2: Add two numbers
a, b = 5, 10
print("Sum:", a + b)

# Exercise 3: Find the square of a number
num = 7
print("Square:", num ** 2)

# Exercise 4: Swap two variables
x, y = 3, 4
x, y = y, x
print("After swapping:", x, y)

# Exercise 5: Check if a number is even or odd
n = 11
print("Even" if n % 2 == 0 else "Odd")

# Exercise 6: Find factorial using loop
fact, n = 1, 5
for i in range(1, n+1):
    fact *= i
print("Factorial:", fact)

# Exercise 7: Reverse a string
s = "Python"
print("Reversed:", s[::-1])

# Exercise 8: Check palindrome
word = "level"
print("Palindrome" if word == word[::-1] else "Not Palindrome")

# Exercise 9: Count vowels in a string
text = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for ch in text if ch in vowels)
print("Vowel Count:", count)

# Exercise 10: Generate Fibonacci series up to 10 terms
fibo = [0, 1]
for i in range(2, 10):
    fibo.append(fibo[-1] + fibo[-2])
print("Fibonacci:", fibo)

# --------------------
# Section 2: Data Structures
# --------------------

# Exercise 11: Find max in a list
nums = [10, 25, 3, 45, 7]
print("Max:", max(nums))

# Exercise 12: Sum of list elements
print("Sum:", sum(nums))

# Exercise 13: Find unique elements in list
dup_list = [1,2,2,3,4,4,5]
unique = list(set(dup_list))
print("Unique:", unique)

# Exercise 14: Sort list in ascending order
print("Sorted:", sorted(nums))

# Exercise 15: Dictionary operations
student = {"name": "Alice", "age": 20}
print(student["name"], student.get("age"))

# Exercise 16: Count frequency of characters in string
text = "banana"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print("Frequency:", freq)

# Exercise 17: Tuple unpacking
t = (10, 20, 30)
a, b, c = t
print("Values:", a, b, c)

# Exercise 18: Merge two dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"c": 3}
d1.update(d2)
print("Merged:", d1)

# Exercise 19: Check if key exists in dict
print("Exists" if "a" in d1 else "Not Exists")

# Exercise 20: List comprehension to square numbers
squares = [x**2 for x in range(6)]
print("Squares:", squares)

# --------------------
# Section 3: Functions & Modules
# --------------------

# Exercise 21: Define a function to add 2 numbers
def add(a, b):
    return a + b
print("Add Function:", add(2,3))

# Exercise 22: Lambda function
square = lambda x: x**2
print("Lambda Square:", square(4))

# Exercise 23: Recursive factorial
def factorial(n):
    return 1 if n==0 else n*factorial(n-1)
print("Recursive Factorial:", factorial(5))

# Exercise 24: Default arguments
def greet(name="Guest"):
    return f"Hello, {name}"
print(greet())
print(greet("Alice"))

# Exercise 25: Import math module
import math
print("Square root:", math.sqrt(16))

# Exercise 26: Use random module
import random
print("Random Number:", random.randint(1, 100))

# Exercise 27: Function to check prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
print("Prime 17?", is_prime(17))

# Exercise 28: Function with *args
def total(*nums):
    return sum(nums)
print("Total:", total(1,2,3,4))

# Exercise 29: Function with **kwargs
def print_info(**info):
    for k,v in info.items():
        print(k, ":", v)
print_info(name="Mohan", age=25)

# Exercise 30: Global vs Local variable
x = 10
def demo():
    global x
    x = 20
demo()
print("Global x:", x)

# --------------------
# Section 4: File Handling & Exceptions
# --------------------

# Exercise 31: Write to file
with open("sample.txt", "w") as f:
    f.write("Hello File")

# Exercise 32: Read file
with open("sample.txt", "r") as f:
    print("File Content:", f.read())

# Exercise 33: Append to file
with open("sample.txt", "a") as f:
    f.write("\nAppended line")

# Exercise 34: Exception handling
try:
    print(10/0)
except ZeroDivisionError:
    print("Cannot divide by zero")

# Exercise 35: Finally block
try:
    num = int("abc")
except ValueError:
    print("Value Error")
finally:
    print("Execution complete")

# Exercise 36: Raise exception
def check_age(age):
    if age < 18:
        raise ValueError("Underage")
    return "Allowed"
try:
    print(check_age(16))
except ValueError as e:
    print(e)

# Exercise 37: File not found handling
try:
    open("nofile.txt")
except FileNotFoundError:
    print("File not found")

# Exercise 38: Using with open for safety
with open("safe.txt", "w") as f:
    f.write("Safe writing")

# Exercise 39: Write list to file
lines = ["line1", "line2", "line3"]
with open("list.txt", "w") as f:
    for l in lines:
        f.write(l + "\n")

# Exercise 40: Read file line by line
with open("list.txt", "r") as f:
    for line in f:
        print("Line:", line.strip())

# --------------------
# Section 5: NumPy, Pandas, Visualization
# --------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Exercise 41: NumPy array creation
arr = np.array([1,2,3,4])
print("Array:", arr)

# Exercise 42: NumPy operations
print("Mean:", arr.mean())

# Exercise 43: NumPy reshape
mat = np.arange(9).reshape(3,3)
print("Matrix:\n", mat)

# Exercise 44: Pandas DataFrame
data = {"Name":["A","B","C"], "Age":[20,21,22]}
df = pd.DataFrame(data)
print(df)

# Exercise 45: Read CSV (dummy example)
df.to_csv("people.csv", index=False)
df2 = pd.read_csv("people.csv")
print("Read CSV:\n", df2)

# Exercise 46: Handle missing values
df2.loc[1,"Age"] = np.nan
print(df2.fillna(0))

# Exercise 47: Group by in Pandas
df3 = pd.DataFrame({"Dept":["IT","HR","IT"], "Salary":[50000,60000,55000]})
print(df3.groupby("Dept")["Salary"].mean())

# Exercise 48: Merge DataFrames
df_a = pd.DataFrame({"id":[1,2], "name":["A","B"]})
df_b = pd.DataFrame({"id":[1,2], "score":[90,80]})
print(pd.merge(df_a, df_b, on="id"))

# Exercise 49: Plot with Matplotlib
plt.plot([1,2,3],[2,4,6])
plt.title("Line Plot")
plt.show()

# Exercise 50: Seaborn visualization
tips = sns.load_dataset("tips")
sns.barplot(x="day", y="total_bill", data=tips)
plt.title("Average Bill per Day")
plt.show()

