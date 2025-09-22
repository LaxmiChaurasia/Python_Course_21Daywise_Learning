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
---
# 🐍 Python Operators — Complete Guide

Operators in Python are **symbols** or **keywords** that perform operations on values or variables.
Just like `+`, `-`, `×`, `÷` in Maths, Python uses operators for **calculations, comparisons, assignments, logic, and more**.

---

## 🔑 Types of Operators in Python

1️⃣ Arithmetic Operators
2️⃣ Assignment Operators
3️⃣ Comparison Operators
4️⃣ Logical Operators
5️⃣ Identity Operators
6️⃣ Membership Operators
7️⃣ Bitwise Operators (Advanced)

---

## 1️⃣ Arithmetic Operators ➕➖✖️➗

👉 Used for **Math operations** (addition, subtraction, etc.)

| Operator | Meaning        | Example  | Output |
| -------- | -------------- | -------- | ------ |
| `+`      | Addition       | `5 + 3`  | `8`    |
| `-`      | Subtraction    | `10 - 4` | `6`    |
| `*`      | Multiplication | `4 * 2`  | `8`    |
| `/`      | Division       | `8 / 2`  | `4.0`  |
| `//`     | Floor Division | `7 // 2` | `3`    |
| `%`      | Modulus        | `7 % 2`  | `1`    |
| `**`     | Exponent       | `2 ** 3` | `8`    |

✅ Example:

```python
a = 10
b = 3
print(a + b)  # 13
print(a ** b) # 1000
```

---

## 2️⃣ Assignment Operators 🖊️

👉 Used to **assign values** to variables

| Operator | Example  | Same As      |
| -------- | -------- | ------------ |
| `=`      | `x = 5`  | Assign value |
| `+=`     | `x += 2` | `x = x + 2`  |
| `-=`     | `x -= 3` | `x = x - 3`  |
| `*=`     | `x *= 2` | `x = x * 2`  |
| `/=`     | `x /= 2` | `x = x / 2`  |

✅ Example:

```python
x = 5
x += 3   # same as x = x + 3
print(x) # 8
```

---

## 3️⃣ Comparison Operators ⚖️

👉 Always return **True** or **False**

| Operator | Meaning       | Example  | Result |
| -------- | ------------- | -------- | ------ |
| `==`     | Equal to      | `5 == 5` | True   |
| `!=`     | Not equal to  | `5 != 3` | True   |
| `>`      | Greater than  | `6 > 3`  | True   |
| `<`      | Less than     | `4 < 2`  | False  |
| `>=`     | Greater/Equal | `5 >= 5` | True   |
| `<=`     | Less/Equal    | `3 <= 2` | False  |

---

## 4️⃣ Logical Operators 🔗

👉 Used to **combine conditions**

| Operator | Meaning                 | Example             | Result |
| -------- | ----------------------- | ------------------- | ------ |
| `and`    | True if both are True   | `(5 > 3 and 4 > 2)` | True   |
| `or`     | True if any one is True | `(5 < 3 or 4 > 2)`  | True   |
| `not`    | Opposite of condition   | `not(5 > 3)`        | False  |

---

## 5️⃣ Identity Operators 🆔

👉 Check if two variables refer to the **same object**

| Operator | Example      | Meaning                         |
| -------- | ------------ | ------------------------------- |
| `is`     | `x is y`     | True if x and y are same object |
| `is not` | `x is not y` | True if x and y are not same    |

---

## 6️⃣ Membership Operators 📖

👉 Check if a value exists inside another (list, string, etc.)

| Operator | Example              | Result |
| -------- | -------------------- | ------ |
| `in`     | `"a" in "apple"`     | True   |
| `not in` | `"x" not in "apple"` | True   |

---

## 7️⃣ Bitwise Operators ⚙️ (Advanced)

👉 Used for **binary operations** (works on 0s and 1s).

| Operator | Meaning     |    |
| -------- | ----------- | -- |
| `&`      | AND         |    |
| \`       | \`          | OR |
| `^`      | XOR         |    |
| `~`      | NOT         |    |
| `<<`     | Left Shift  |    |
| `>>`     | Right Shift |    |

---

## 🎓 Real Life Example

```python
price = 100
discount = 20
final_price = price - discount
print("Final Price is", final_price)
```

✅ Output:

```
Final Price is 80
```

---

## 📘 Summary

* **Arithmetic** → `+ - * / // % **`
* **Assignment** → `= += -= *= ...`
* **Comparison** → `== != > < >= <=`
* **Logical** → `and or not`
* **Identity** → `is, is not`
* **Membership** → `in, not in`
* **Bitwise** → `& | ^ ~ << >>`

👉 By mastering operators, you unlock the **foundation of Python programming** 🚀

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





