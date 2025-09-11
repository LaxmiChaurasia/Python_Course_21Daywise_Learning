# Day05: Python Basics — Variables, Numbers and Strings 🔢🔤

## Topics Covered
- 5.1: Variables 📦
- 5.2: Numbers 🔢
- 5.3: Strings 🔤
- 5.4: Quiz — Variables, Numbers and Strings ❓
- 5.5: Mr. Beginner & Mr. Expert 🧑‍💻👨‍🏫
- 5.6: Exercise — Variables, Numbers and Strings 📝

In this section, we explore the **building blocks of Python programming** — Variables, Numbers, and Strings.  
You’ll learn how to store values, work with numeric data, and manipulate text.  


---

## 5.1: Variables 📦
- Variables are containers for storing data.
- Python automatically detects the type.

```python
name = "Alice"     # String
age = 25           # Integer
height = 5.6       # Float
is_student = True  # Boolean
````

---

## 5.2: Numbers 🔢

* Types: Integer, Float, Complex
* Common operations: `+`, `-`, `*`, `/`, `//`, `%`, `**`

```python
a = 10
b = 3.5

print(a + b)   # 13.5
print(a * b)   # 35.0
print(a // 3)  # 3 (floor division)
```

---

## 5.3: Strings 🔤

* Strings store text data.
* Support slicing & built-in functions.

```python
message = "Hello, Python!"

print(message.upper())      # HELLO, PYTHON!
print(message.lower())      # hello, python!
print(message[0:5])         # Hello
print("Python" in message)  # True
```

---

## 5.4: Quiz — Variables, Numbers and Strings ❓

**Q1.** Which of these is a valid variable name?

* `1name`, `name1`, `first-name`, `_score`

**Q2.** What will `5 // 2` return?

* `2` or `2.5`?

**Q3.** What is the output of:

```python
text = "Python"
print(text[2:5])
```

---

### ✅ Quiz Answers

* **Q1:** `name1` and `_score` ✅
* **Q2:** `2` ✅ (floor division gives integer result)
* **Q3:** `tho` ✅

---

## 5.5: Mr. Beginner & Mr. Expert 🧑‍💻👨‍🏫

* **Beginner:** "Variables and strings scare me!"
* **Expert:** "Think of variables as boxes, numbers as math, and strings as words. Practice removes fear."

---

## 5.6: Exercise — Variables, Numbers and Strings 📝

**Exercise 1:**
Create 3 variables: `food = 120.50`, `rent = 500.40`, `utilities = 200.75`.
Find total monthly expense.

**Solution:**

```python
food = 120.50
rent = 500.40
utilities = 200.75

total = food + rent + utilities
print("Total Monthly Expense:", total)  # 821.65
```

---

**Exercise 2:**
Store your first name and last name in two variables. Combine into one full name using f-string.

**Solution:**

```python
first = "Mohan"
last = "Sharma"

name = f"{first} {last}"
print("Full Name:", name)  # Mohan Sharma
```

---

**Exercise 3:**
Write a string `"DataScience"` and use slicing to print `"Data"`, `"Science"`, and `"DS"`.

**Solution:**

```python
s = "DataScience"

print(s[0:4])    # Data
print(s[4:])     # Science
print(s[0] + s[4])  # DS
```

---

## 5.7: Chapter Summary 📘

* Variables store data without declaring types.
* Numbers → Integers, Floats, Complex.
* Strings → Text data, slicing, built-in methods.
* Practice with quizzes & exercises makes concepts **easy & fear-free**.

---

✅ By completing Day05, you’ve built a **strong foundation** in Variables, Numbers, and Strings. 🚀







