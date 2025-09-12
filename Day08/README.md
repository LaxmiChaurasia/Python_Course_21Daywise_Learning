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

Got it 👍 I’ll break down **Chapter 8: Python Basics — Classes and Exception Handling** step by step in **easy and simple language**, formatted neatly for your **GitHub README repository**.

Here’s the detailed explanation:

---

# Day08: Python Basics — Classes and Exception Handling 🏗⚠️

## Topics Covered

* 8.1: Classes and Objects 🧑‍💻
* 8.2: Operator Overloading ➕
* 8.3: Inheritance 👨‍👩‍👧
* 8.4: Exception Handling ⚠️
* 8.5: `__main__` Function 🏁
* 8.6: Quiz — Classes & Exception Handling ❓
* 8.7: Using Python in Real-Time Problem 🌍
* 8.8: Exercise — Classes & Exception Handling 📝
* 8.9: Chapter Summary (Thumbnail 📘)

---

## 8.1: Classes and Objects 🧑‍💻

* A **class** is like a blueprint (design).
* An **object** is something built using that blueprint.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

mycar = Car("Toyota", "Fortuner")
print(mycar.brand)   # Toyota
```

✅ Here, `Car` is the class and `mycar` is the object.

---

## 8.2: Operator Overloading ➕

* Python allows you to use operators (`+`, `-`, `*`, etc.) in a customized way for objects.

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

a = Number(10)
b = Number(20)
print(a + b)   # 30
```

✅ We changed how the `+` operator works for `Number` objects.

---

## 8.3: Inheritance 👨‍👩‍👧

* **Inheritance** lets one class use features of another class.
* Saves time & avoids repeating code.

```python
class Animal:
    def speak(self):
        print("This is an animal")

class Dog(Animal):
    def speak(self):
        print("Bark! 🐶")

d = Dog()
d.speak()   # Bark! 🐶
```

✅ `Dog` inherited from `Animal`.

---

## 8.4: Exception Handling ⚠️

* Errors (exceptions) stop programs.
* We can **handle** them using `try-except`.

```python
try:
    x = int("Hello")   # Error
except ValueError:
    print("Invalid number input!")
```

✅ Prevents program crash.

---

## 8.5: `__main__` Function 🏁

* Python uses `__name__ == "__main__"` to check if code is run **directly** or **imported**.

```python
def greet():
    print("Hello!")

if __name__ == "__main__":
    greet()
```

✅ Runs only if file is executed directly.

---

## 8.6: Quiz — Classes & Exception Handling ❓

**Q1.** Which one is correct for creating a class?

* a) `class MyClass:` ✅
* b) `MyClass = class`
* c) `def class MyClass`

**Q2.** What will happen if exception is not handled?

* a) Program stops ✅
* b) Program skips error silently
* c) Program continues

---

## 8.7: Using Python in Real-Time Problem 🌍

**Problem:** Build a banking system where users can deposit and withdraw money.

```python
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

acc = BankAccount("Mohan", 1000)
acc.deposit(500)
acc.withdraw(2000)   # Insufficient funds!
```

✅ Real-world simulation with **Classes + Exception Handling**.

---

## 8.8: Exercise — Classes and Exception Handling 📝

**Exercise 1:**
Create a class `Student` with attributes `name`, `marks`. Add method `show_result()` that prints "Pass" if marks ≥ 40 else "Fail".

**Exercise 2:**
Create a class `Calculator` that overloads `+` and `-` operators.

**Exercise 3:**
Write a program that asks user for a number. If user enters non-number, handle error using `try-except`.

---

## 8.9: Thumbnail 📘

📦 **Classes** → Blueprint for objects.
➕ **Operator Overloading** → Redefine operators for custom objects.
👨‍👩‍👧 **Inheritance** → Reuse code from parent class.
⚠️ **Exception Handling** → Handle errors safely with `try-except`.
🏁 **`__main__`** → Run code only when executed directly.

✅ With these concepts, you can now write **object-oriented programs** and handle errors **professionally**. 🚀

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




