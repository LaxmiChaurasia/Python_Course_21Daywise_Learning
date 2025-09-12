# Day12: Python Advanced — Comprehensions and Sets 🐍✨

## Topics Covered

- 12.1: Introduction
- 12.2: Set and Frozenset
- 12.3: Lists, Dict, and Set Comprehensions
- 12.4: Quiz — Comprehensions and Sets ❓
- 12.5: Mr. Beginner’s Adhoc Tasks 🧑‍💻
- 12.6: Exercise — Comprehensions and Sets 📝
- 12.7: PEP8 Naming Convention
- 12.8: Code Debugging Using PyCharm 🐞
- 12.9: Chapter Summary 📘

---

## 12.1: Introduction

* Advanced Python topics help you **write concise, readable, and efficient code**.
* Comprehensions allow you to **create lists, dictionaries, or sets in a single line**.
* Sets are **unordered collections of unique elements**, useful for removing duplicates and performing mathematical operations.

---

## 12.2: Set and Frozenset

-Set: mutable collection, no duplicate values.

```python
fruits = {"apple", "banana", "mango"}
fruits.add("orange")
fruits.remove("banana")
print(fruits)
```

-Frozenset: immutable version of set.

```python
frozen_fruits = frozenset(["apple", "banana", "mango"])
print(frozen_fruits)
```

---

## 12.3: List, Dictionary, and Set Comprehensions

**List Comprehension**

* Create lists in a concise way:

```python
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

**Dictionary Comprehension**

* Create dictionaries easily:

```python
square_dict = {x: x**2 for x in range(1, 6)}
print(square_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

**Set Comprehension**

* Create sets using comprehension:

```python
even_set = {x for x in range(10) if x % 2 == 0}
print(even_set)  # {0, 2, 4, 6, 8}
```

---

## 12.4: Quiz — Comprehensions and Sets ❓

**Q1:** Which comprehension creates a set of squares of numbers 1–5?
**Q2:** What is the difference between `set` and `frozenset`?
**Q3:** Predict the output:

```python
nums = [1, 2, 3, 4]
result = {x*2 for x in nums if x%2==0}
print(result)
```

### ✅ Answers:

-Q1:** `{x**2 for x in range(1,6)}`
-Q2:** `set` is mutable; `frozenset` is immutable.
-Q3:** `{4, 8}`

---

## 12.5: Mr. Beginner’s Adhoc Tasks 🧑‍💻

* Mr. Beginner is assigned tasks like:

  * Extracting unique values from lists
  * Generating squares, cubes, or even filtered results
* Comprehensions and sets simplify these tasks in **one line of code**.

---

## 12.6: Exercise — Comprehensions and Sets 📝

**Exercise 1:** Create a list of even numbers from 1 to 20.

```python
even_numbers = [x for x in range(1,21) if x % 2 == 0]
print(even_numbers)
```

**Exercise 2:** Create a dictionary mapping numbers to their cubes.

```python
cubes = {x: x**3 for x in range(1, 6)}
print(cubes)
```

**Exercise 3:** Remove duplicates from a list using set comprehension.

```python
nums = [1,2,2,3,4,4,5]
unique_nums = {x for x in nums}
print(unique_nums)
```

---

## 12.7: PEP8 Naming Convention

* Follow **snake\_case** for variables and functions.
* Constants should be **UPPERCASE**.
* Example:

```python
max_value = 100
def calculate_area(radius):
    return 3.14 * radius**2
```

---

## 12.8: Code Debugging Using PyCharm 🐞

* Use **breakpoints** to pause execution.
* Inspect variables and outputs step by step.
* Helps identify **logical and runtime errors** efficiently.

---

## 12.9: Chapter Summary 📘

* Comprehensions = **concise way to create lists, sets, dictionaries**
* Sets = **unique, unordered collections**
* Frozensets = **immutable sets**
* PEP8 ensures **clean and readable code**
* Debugging = **critical skill to fix errors and validate logic**

✅ By completing Day12, you can **write efficient Python code** for real-time tasks, filtering, and data transformation. 🚀

---
