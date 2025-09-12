# Day07: Functions, Dictionaries, Tuples and File Handling 🧩

## Topics Covered

* 7.1: Functions
* 7.2: Dictionaries & Tuples
* 7.3: Modules & pip
* 7.4: File Handling
* 7.5: Quiz: Functions, Dictionaries, Tuples & File Handling
* 7.6: Mr. Beginner’s Request to Mr. Expert
* 7.7: Exercises + Solutions
* 7.8: Two Deadly Viruses Infecting Learners (and fixes)
* 7.9: Thumbnail

---

## ✅ 7.1 Functions — Stepwise (what, why, how)

**What is a function?**
A function is a named block of code that does one job. Use functions to **reuse code**, **organize logic**, and make programs readable.

### Step 1 — Define a simple function

```python
def greet():
    """Print a greeting message."""
    print("Hello! Welcome to functions.")
```

### Step 2 — Call (use) the function

```python
greet()  # runs the code inside greet
```

### Step 3 — Function with parameters and return value

```python
def add(a, b):
    return a + b

result = add(5, 7)  # result = 12
```

### Step 4 — Default arguments, keyword args

```python
def greet_person(name="Guest"):
    print(f"Hello, {name}!")

greet_person()           # Hello, Guest!
greet_person("Mohan")    # Hello, Mohan!
```

### Step 5 — Variable arguments (`*args`, `**kwargs`)

```python
def sum_all(*args):
    total = 0
    for n in args:
        total += n
    return total

def print_info(**kwargs):
    for k,v in kwargs.items():
        print(k, ":", v)
```

### Step 6 — Docstring and small best practices

* Always add a one-line docstring describing what the function does.
* Keep functions short (single responsibility).
* Use meaningful parameter names.

---

## ✅ 7.2 Dictionaries & Tuples — Stepwise

### Dictionaries (key → value)

**Use when**: you need to map a key to a value (like name → age).

#### Step 1 — Create & access

```python
student = {"name": "Asha", "age": 16, "grade": "A"}
print(student["name"])         # Asha
print(student.get("score"))    # None (safer than [] if key might not exist)
```

#### Step 2 — Useful methods

```python
student["score"] = 95          # add or update
student.update({"city": "Jodhpur"})
keys = student.keys()
values = student.values()
items = student.items()
age = student.pop("age")       # remove and return value
```

#### Step 3 — Looping through dict

```python
for k, v in student.items():
    print(k, "->", v)
```

### Tuples (immutable ordered collections)

**Use when**: collection must not change (safe for fixed data).

#### Step 1 — Create & access

```python
t = (1, 2, 3)
single = (5,)   # single-element tuple needs the comma
print(t[0])     # 1
```

#### Step 2 — Unpacking

```python
x, y, z = t
```

#### Step 3 — When to prefer tuple over list

* Use tuple for fixed data (like coordinates), or when you want immutability and a tiny performance boost.

---

## ✅ 7.3 Modules & pip — Stepwise

**What is a module?** — A `.py` file with functions/classes you can import.

### Step 1 — Make a simple module

Create a file `mymath.py`:

```python
# mymath.py
def add(a, b):
    return a + b
```

Use it in another file:

```python
from mymath import add
print(add(2,3))   # 5
```

### Step 2 — Use pip to install packages

* Install package:

```bash
pip install requests
```

* Check installed packages:

```bash
pip freeze
```

* Save requirements:

```bash
pip freeze > requirements.txt
```

* Install from requirements:

```bash
pip install -r requirements.txt
```

### Step 3 — Virtual environment (recommended)

```bash
# create venv
python -m venv .venv
# activate (Windows)
.venv\Scripts\activate
# activate (mac/linux)
source .venv/bin/activate
```

---

## ✅ 7.4 File Handling — Stepwise (read/write safely)

**Modes**: `'r'` read, `'w'` write (overwrite), `'a'` append, `'x'` create, add `'b'` for binary.

### Step 1 — Read whole file

```python
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()
print(text)
```

### Step 2 — Read line by line

```python
with open("data.txt") as f:
    for line in f:
        print(line.strip())
```

### Step 3 — Write to a file

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")
    f.writelines(["line2\n", "line3\n"])
```

### Step 4 — Append to a file

```python
with open("output.txt", "a") as f:
    f.write("Another line\n")
```

### Step 5 — CSV basic (using csv module)

```python
import csv

# write
rows = [["name","age"], ["Asha", 16], ["Mohan", 25]]
with open("people.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# read
with open("people.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

### Step 6 — Exception-safe file handling

Use `with open(...)` — it automatically closes file even on error. For extra safety:

```python
try:
    with open("data.txt") as f:
        process(f)
except FileNotFoundError:
    print("File not found.")
```

---

## ✅ 7.5 Quiz — Quick Questions (with answers below)

**Q1.** What does this print?

```python
def f(x=2):
    return x * 2
print(f()) 
```

**Q2.** Which data type is best for key → value mapping?
`list`, `tuple`, `dict` ?

**Q3.** How do you open a file to add content without deleting existing text?

**Q4.** True or False: Tuples are mutable.

**Q5.** How to install a package named `pandas`?

### ✅ Quiz Answers

* **A1:** `4` — default `x=2` so `2*2=4`.
* **A2:** `dict`.
* **A3:** Use append mode: `open("file.txt", "a")`.
* **A4:** False — tuples are immutable.
* **A5:** `pip install pandas`.

---

## ✅ 7.6 Mr. Beginner’s Request → Mr. Expert (short dialogue)

**Beginner:** “I’m confused — where should I put functions and how to read a CSV for analysis?”
**Expert:**

1. Put reusable functions in a module (a separate `.py` file) and import them.
2. For CSVs, start with the `csv` module; later use `pandas.read_csv()` for easier analysis.
3. Use `with open(...)` for file safety.
4. Test small parts: write a function, test it, then use it on the full file.

---

## ✅ 7.7 Exercises — Stepwise Tasks & Solutions

**Exercise 1 — Function practice**
*Write a function `multiply_list(nums)` that multiplies all numbers in a list and returns product.*

**Solution**

```python
def multiply_list(nums):
    product = 1
    for n in nums:
        product *= n
    return product

print(multiply_list([2,3,4]))  # 24
```

**Exercise 2 — Dictionary practice**
*Given `sales = [("tomato", 5), ("apple", 3), ("tomato", 2)]`, create a dict with totals.*

**Solution**

```python
sales = [("tomato", 5), ("apple", 3), ("tomato", 2)]
totals = {}
for item, qty in sales:
    totals[item] = totals.get(item, 0) + qty
print(totals)  # {'tomato': 7, 'apple': 3}
```

**Exercise 3 — File handling practice**
*Write a program that reads `numbers.txt` (one number per line) and prints the sum.*

**Solution**

```python
total = 0
with open("numbers.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            total += float(line)
print("Total:", total)
```

---

## ✅ 7.8 Two Deadly Viruses Infecting Learners — and how to cure them

These are common learning pitfalls presented like “viruses” so you remember them.

### Virus 1 — **Perfectionism (Fear of mistakes)**

* **Symptoms:** You avoid coding until it’s “perfect”, you fear errors.
* **Cure:** Embrace small steps. Write minimal code, run it, fix errors. Treat bugs as learning signals. Use version control (git) so you can experiment safely.

### Virus 2 — **Procrastination (Inconsistent practice)**

* **Symptoms:** Lots of planning but little coding; long gaps between practice sessions.
* **Cure:** Make tiny daily commitments (15–30 mins). Use checklists on GitHub, set small goals (one function, one file), and celebrate small wins.

---

## ✅ 7.9 Thumbnail (simple & clear)

* **Functions** let you organize and reuse code — learn parameters, return values, default args, and `*args/**kwargs`.
* **Dictionaries** map keys to values — ideal for quick lookups; **tuples** are immutable ordered groups.
* **Modules & pip** let you split code and use external packages; prefer virtual environments (`venv`).
* **File handling** is essential: use `with open(...)` for safe reading/writing; use `csv` for tabular data.
* Practice small functions, read and write simple files, and use dictionaries for aggregation — these skills are building blocks for data projects.

---

## 👩‍💻 Suggested repository structure for Day07

```
Day07/
├─ README.md         # (paste this content)
├─ examples.py       # function, dict, tuple examples
├─ file_examples.py  # read/write and csv examples
├─ exercises.py      # exercise code & solutions
└─ numbers.txt       # sample data for file exercises
```

