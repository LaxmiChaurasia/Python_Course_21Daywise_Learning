# Day08: Python Basics — Classes and Exception Handling 🐍⚡

## Topics Covered
- 8.1: Classes and Objects 🧑‍🎓
- 8.2: Operator Overloading ➕
- 8.3: Inheritance 🐶
- 8.4: Exception Handling ⚠️
- 8.5: __main__ Function 🎯
- 8.6: Quiz ❓
- 8.7: Real-Time Problem Solving 💡
- 8.8: Exercises 📝
- 8.9: Chapter Summary 🏆


---

# 📂 Folder Structure

```
Day08/
 ├── classes_examples.py        # Classes, Objects, Inheritance, Operator Overloading
 ├── exception_examples.py      # Exception handling examples
 ├── exercises.py               # Hands-on practice tasks
 ├── main_function_demo.py      # __main__ function usage
 └── README.md                  # Overview + Quiz + Summary
```

---

# 📝 1. classes\_examples.py

```python
# Day08 - Classes, Objects, Inheritance, Operator Overloading

# -------------------------------
# 8.1 Classes and Objects
# -------------------------------
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        return f"Student: {self.name}, Marks: {self.marks}"

s1 = Student("Amit", 85)
print(s1.display())


# -------------------------------
# 8.2 Operator Overloading
# -------------------------------
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
print("v1 + v2 =", v1 + v2)


# -------------------------------
# 8.3 Inheritance
# -------------------------------
class Animal:
    def speak(self):
        return "This animal makes a sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

d = Dog()
print(d.speak())  # Woof!
```

---

# 📝 2. exception\_examples.py

```python
# Day08 - Exception Handling

# -------------------------------
# 8.4 Exception Handling
# -------------------------------
try:
    num = int("abc")  # invalid conversion
except ValueError as e:
    print("Error:", e)
finally:
    print("Execution Completed ✅")


# Multiple exceptions
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed")
except Exception as e:
    print("Unexpected error:", e)


# Custom Exception
class NegativeNumberError(Exception):
    pass

def check_number(n):
    if n < 0:
        raise NegativeNumberError("Negative number not allowed")
    else:
        print("Number is valid:", n)

try:
    check_number(-5)
except NegativeNumberError as e:
    print("Custom Error:", e)
```

---

# 📝 3. exercises.py

```python
# Day08 - Exercises

# -------------------------------
# Exercise 1: Class
# -------------------------------
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        return f"{self.name} earns ₹{self.salary}"

emp1 = Employee("Ravi", 50000)
print(emp1.display())


# -------------------------------
# Exercise 2: Operator Overloading
# -------------------------------
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def __add__(self, other):
        return BankAccount(self.balance + other.balance)
    
    def __str__(self):
        return f"Balance: ₹{self.balance}"

acc1 = BankAccount(10000)
acc2 = BankAccount(20000)
acc3 = acc1 + acc2
print(acc3)


# -------------------------------
# Exercise 3: Exception Handling
# -------------------------------
try:
    marks = int(input("Enter marks: "))
    if marks < 0:
        raise ValueError("Marks cannot be negative")
    print("Marks entered:", marks)
except ValueError as e:
    print("Error:", e)
```

---

# 📝 4. main\_function\_demo.py

```python
# Day08 - __main__ Function

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Code runs only when file is executed directly
if __name__ == "__main__":
    print("Running as main script")
    print("Addition:", add(10, 5))
    print("Subtraction:", subtract(10, 5))
```

---



