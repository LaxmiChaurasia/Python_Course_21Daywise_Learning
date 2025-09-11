# Day06: Python Basics — Lists, If Condition & For Loop ✅


## Topics Covered
- 6.1 Lists 📋 — Stepwise Guide
- 6.2 Install PyCharm 🛠️ — Stepwise (Community Edition)
- 6.3 If Condition 🧭 — Stepwise
- 6.4 For Loop 🔁 — Stepwise
- 6.5 Quiz: Lists, If Condition and For Loop ❓
- 6.6 Mr. X Found Something Interesting to Practice — Story + Task ✨
- 6.7 Exercises — With Stepwise Solutions
- 6.8 Chapter Summary ✔️


This lesson covers three essential building blocks of Python: **lists** (flexible containers), **if conditions** (decision making), and **for loops** (repetition).
Below is a step-by-step, GitHub-ready guide with examples, quizzes, practice story, exercises and solutions.

---

## 6.1 Lists 📋 — Stepwise Guide

**What is a list?**
A list is an ordered, mutable collection of items (can be different types).

### Step 1 — Create lists

```python
empty = []
nums = [1, 2, 3, 4]
mixed = ["apple", 10, 3.14, True]
nested = [[1,2], ["a","b"]]
```

### Step 2 — Access items (indexing & slicing)

```python
a = nums[0]      # 1
b = nums[-1]     # 4
slice_ = nums[1:3]  # [2, 3]
```

### Step 3 — Common list methods (useful stepwise)

* `append(x)` — add at end
* `insert(i, x)` — insert at index
* `extend(iterable)` — add many
* `pop(i)` / `pop()` — remove & return
* `remove(x)` — remove first match
* `index(x)` — find position
* `count(x)` — count occurrences
* `sort()` / `sorted()` — sort in place / new list
* `reverse()` — reverse in place
* `copy()` — shallow copy
* `clear()` — empty list

Examples:

```python
fruits = ["apple", "banana"]
fruits.append("mango")        # ["apple","banana","mango"]
fruits.insert(1, "orange")    # ["apple","orange","banana","mango"]
x = fruits.pop()              # removes "mango"
fruits.remove("orange")       # removes first "orange"
```

### Step 4 — Iterate lists using `for` (preferred for calculations)

```python
total = 0
prices = [10, 20, 30]
for p in prices:
    total += p
print(total)  # 60
```

### Step 5 — List comprehension (shorter, but equivalent logic can use for-loop)

```python
squares = [x*x for x in range(1, 6)]  # [1,4,9,16,25]
# Equivalent using for-loop (preferred for step-by-step clarity)
squares2 = []
for x in range(1,6):
    squares2.append(x*x)
```

### Step 6 — Nested lists and nested loops

```python
matrix = [[1,2,3],[4,5,6]]
for row in matrix:
    for val in row:
        print(val, end=" ")
# output: 1 2 3 4 5 6
```

### Tip: Lists are mutable — assignment vs copy

```python
a = [1,2,3]
b = a         # b is same object
c = a.copy()  # shallow copy
```

---

## 6.2 Install PyCharm 🛠️ — Stepwise (Community Edition)

**Step 1:** Download

* Visit JetBrains → *PyCharm → Download* → choose **Community** (free).

**Step 2:** Install (Windows)

1. Run `.exe` installer.
2. Choose install location, optionally add **"Add to PATH"** and create desktop shortcut.
3. Finish and launch PyCharm.

**Step 3:** Install (Mac)

1. Open `.dmg`, drag PyCharm to Applications.
2. Launch PyCharm from Applications.

**Step 4:** Install (Linux)

* Use JetBrains Toolbox or download tarball and run `pycharm.sh`.
* On Ubuntu you can also use `snap`:

  ```bash
  sudo snap install pycharm-community --classic
  ```

**Step 5:** Configure interpreter & project

1. Create New Project → set **Virtualenv** or choose system Python.
2. If using virtualenv, PyCharm will create `.venv` automatically.
3. Create new Python file, run `print("Hello, PyCharm!")`.

**Tips**

* Keep `Project Interpreter` pointed to Python 3.x.
* Install helpful plugins (e.g., Markdown, Git).
* Use PyCharm for larger projects; use Jupyter for data notebooks.

---

## 6.3 If Condition 🧭 — Stepwise

**Step 1 — Basic `if` syntax**

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

**Step 2 — `if-else`**

```python
if x % 2 == 0:
    print("even")
else:
    print("odd")
```

**Step 3 — `if-elif-else` chain**

```python
marks = 75
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "D"
print(grade)
```

**Step 4 — Logical operators**

* `and`, `or`, `not`

```python
age = 20
if age >= 18 and age < 60:
    print("adult")
```

**Step 5 — Membership & identity**

```python
colors = ["red","green"]
if "red" in colors:
    print("found")
```

**Step 6 — Truthy / Falsy**

* Falsy: `0`, `0.0`, `""`, `[]`, `{}`, `None`, `False`

```python
s = ""
if not s:
    print("empty string")
```

**Common pitfalls**

* Use `==` for comparison, not `=` (assignment).
* Indentation matters; use consistent 4 spaces.
* Colon `:` necessary after condition.

---

## 6.4 For Loop 🔁 — Stepwise

**Step 1 — Basic iteration over list**

```python
fruits = ["apple", "banana", "mango"]
for f in fruits:
    print(f)
```

**Step 2 — Loop with `range()`**

```python
for i in range(5):       # 0,1,2,3,4
    print(i)
for i in range(1,6):     # 1..5
    print(i)
```

**Step 3 — `enumerate()` to get index & value**

```python
for idx, val in enumerate(fruits, start=1):
    print(idx, val)
```

**Step 4 — `zip()` to iterate multiple lists**

```python
names = ["A","B"]
scores = [90, 80]
for n, s in zip(names, scores):
    print(n, s)
```

**Step 5 — Loop control: `break`, `continue`, `else`**

```python
for x in range(5):
    if x == 3:
        break      # exits loop
    if x % 2 == 0:
        continue   # skip to next iteration
else:
    print("Finished without break")  # runs only if loop didn't break
```

**Step 6 — Iterating dicts**

```python
d = {"a":1, "b":2}
for k in d:          # iterates keys
    print(k, d[k])
for k,v in d.items():
    print(k, v)
```

**Step 7 — Using `for` for calculations (user preference)**

```python
nums = [2,4,6]
total = 0
for n in nums:
    total += n
print(total)
```

---

## 6.5 Quiz: Lists, If Condition and For Loop ❓

**Q1.** What is the result of:

```python
lst = [1,2,3]
lst.append([4,5])
print(len(lst))
```

**Q2.** What does `lst.pop()` return if `lst = [10, 20, 30]`?

**Q3.** What is printed by:

```python
for i in range(2):
    for j in range(2):
        print(i, j)
```

**Q4.** What is wrong with this condition?

```python
if x = 5:
    print("x is 5")
```

**Q5.** What will this print?

```python
nums = [1,2,3,4]
for n in nums:
    if n % 2 == 0:
        print(n)
        break
else:
    print("No even")
```

---

### Quiz Answers

* **A1:** `3` — because `.append([4,5])` adds one element (a list) making list `[1,2,3,[4,5]]`.
* **A2:** `30` — `pop()` removes and returns the last item.
* **A3:**

```
0 0
0 1
1 0
1 1
```

* **A4:** Use `==` for comparison. `=` is assignment → SyntaxError.
* **A5:** `2` — loop prints the first even value and `break` prevents `else` from running.

---

## 6.6 Mr. X Found Something Interesting to Practice — Story + Task ✨

**Story:**
Mr. X is a shopkeeper. At day end he has a list of sales per hour: `[5, 8, 6, 0, 10]`. He wants to:

1. Calculate total sales.
2. Find which hours had zero sales.
3. Print a message if any hour had zero sales.

**Stepwise practice tasks**

1. Create the `sales` list.
2. Use a `for` loop to sum sales.
3. Use `if` inside loop to detect zero sales.
4. Print result.

**Starter code**

```python
sales = [5, 8, 6, 0, 10]
total = 0
zero_hours = []
for idx, s in enumerate(sales, start=1):
    total += s
    if s == 0:
        zero_hours.append(idx)
print("Total:", total)
if zero_hours:
    print("Zero sales at hours:", zero_hours)
else:
    print("No zero sales")
```

---

## 6.7 Exercises — With Stepwise Solutions

### Exercise 1 (Beginner)

**Task:** Given `nums = [2,3,5,7,11]` compute the sum using a `for` loop.

**Solution**

```python
nums = [2,3,5,7,11]
s = 0
for n in nums:
    s += n
print(s)  # 28
```

---

### Exercise 2 (Intermediate)

**Task:** From `items = ["apple", "banana", "apple", "mango"]` create a dict with counts using a `for` loop.

**Solution**

```python
items = ["apple", "banana", "apple", "mango"]
counts = {}
for it in items:
    if it in counts:
        counts[it] += 1
    else:
        counts[it] = 1
print(counts)  # {'apple':2, 'banana':1, 'mango':1}
```

---

### Exercise 3 (Intermediate) — Use lists + if + for

**Task:** Filter positive numbers from `arr = [-2, 0, 3, -1, 5]` into `positives` using a `for` loop.

**Solution**

```python
arr = [-2, 0, 3, -1, 5]
positives = []
for x in arr:
    if x > 0:
        positives.append(x)
print(positives)  # [3, 5]
```

---

### Exercise 4 (Advanced)

**Task:** Given a matrix, compute the sum of diagonal elements:

```python
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
```

**Solution**

```python
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
diag_sum = 0
for i in range(len(matrix)):
    diag_sum += matrix[i][i]
print(diag_sum)  # 1 + 5 + 9 = 15
```

---

### Exercise 5 (Challenge)

**Task:** Remove duplicates from a list while preserving order (use `for` loop).

**Solution**

```python
orig = [3,1,2,3,2,4]
seen = set()
result = []
for x in orig:
    if x not in seen:
        result.append(x)
        seen.add(x)
print(result)  # [3,1,2,4]
```

---

## 6.8 Chapter Summary ✔️

* **Lists**

  * Ordered, mutable, support many methods (`append`, `pop`, `extend`, etc.)
  * Use `for` loops to process items step-by-step
  * List comprehensions are concise alternatives

* **If Conditions**

  * `if`, `elif`, `else` for branching
  * Use logical operators and membership checks
  * Watch out for `=` vs `==`, indentation, and truthy/falsy values

* **For Loops**

  * Iterate sequences (`list`, `range`, `dict.items()`, `string`)
  * Useful constructs: `enumerate`, `zip`, `break`, `continue`, `else`
  * Prefer `for` loops for stepwise calculations (clear and testable)



