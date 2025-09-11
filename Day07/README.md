# Day07: Functions, Dictionaries, Tuples and File Handling

## Topics Covered
- 7.1: Functions — Stepwise
- 7.2: Dictionary & Tuples — Stepwise
- 7.3: Modules & pip — Stepwise
- 7.4: File Handling — Stepwise
- 7.5: Quiz — Functions, Dictionaries, Tuples & File Handling
- 7.6: Mr.Beginner’s Request to Mr.Expert — Real-world Task (stepwise + solution)
- 7.7: Exercises — Stepwise + Solutions
- 7.8: Two Deadly Viruses Infecting Learners (metaphor + remedies)
- 7.9: Thumbnail
 

# Day07: Python Basics — Functions, Dictionaries, Tuples & File Handling (Stepwise, Detailed)

This chapter covers functions (design + best practice), dictionaries & tuples (data containers), modules & `pip` (package management), file I/O (text, CSV, JSON).
Each sub-section is **stepwise**, includes clear examples (using `for` loops for calculations when appropriate), quizzes, a small real-world task (Mr.Beginner → Mr.Expert), exercises with solutions, common pitfalls, and a concise business-style chapter summary.

---

## 7.1: Functions — Stepwise

**What a function is:** a named block of reusable code that receives inputs (arguments), performs work, and optionally returns a result.

### Step 1 — Basic function structure

```python
def greet(name):
    """Return a greeting string for name."""
    return f"Hello, {name}!"
```

### Step 2 — Parameters, defaults, keyword args

```python
def book_summary(title, author="Unknown", pages=0):
    """Create a short summary string."""
    return f"{title} by {author} — {pages} pages"
```

### Step 3 — Positional vs keyword arguments

```python
book_summary("Python 101", pages=250)  # positional + keyword
```

### Step 4 — Variable-length args: `*args` and `**kwargs`

```python
def sum_numbers(*nums):
    total = 0
    for n in nums:          # user preference: compute with for-loop
        total += n
    return total

def describe_person(**attrs):
    for k, v in attrs.items():
        print(k, ":", v)
```

### Step 5 — Docstrings and type hints (good practice)

```python
def add(a: float, b: float) -> float:
    """Return a + b."""
    return a + b
```

### Step 6 — Lambda (one-liner) — use sparingly

```python
double = lambda x: x * 2
```

### Step 7 — Higher-order functions (passing functions)

```python
def apply_to_list(fn, items):
    result = []
    for x in items:
        result.append(fn(x))
    return result

def square(x): return x * x
apply_to_list(square, [1,2,3])  # [1,4,9]
```

### Best practices

* Keep functions short (single responsibility).
* Use meaningful names and docstrings.
* Prefer explicit returns.
* Write unit tests for complex functions.

---

## 7.2: Dictionary & Tuples — Stepwise

### Dictionaries (mutable mapping of key → value)

**Step 1 — Create and access**

```python
d = {"name": "Alice", "age": 30}
print(d["name"])   # Alice
```

**Step 2 — Safe access**

```python
print(d.get("salary", 0))    # returns 0 if key not present
```

**Step 3 — Add/Update/Delete**

```python
d["city"] = "Delhi"     # add or update
d.pop("age")            # remove and return value
```

**Step 4 — Iterate**

```python
for k, v in d.items():
    print(k, "=", v)
```

**Step 5 — Useful methods**

* `keys()`, `values()`, `items()`, `update()`, `setdefault()`, `popitem()`.

**Step 6 — Dictionary comprehension**

```python
squares = {i: i*i for i in range(1,6)}  # {1:1, 2:4, ...}
```

**Use-cases**

* Fast lookup, flexible records, counts (frequency maps).

---

### Tuples (immutable ordered collection)

**Step 1 — Create**

```python
t = (1, 2, 3)
single = (5,)   # note trailing comma for single-element tuple
```

**Step 2 — Unpacking**

```python
a, b, c = t
```

**Step 3 — Why tuple?**

* Immutable → safe to use as keys in dicts (if elements are hashable).
* Slightly faster than list for fixed collections.

**Step 4 — Named tuple (for clarity)**

```python
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(2, 3)
```

**When to use which?**

* Use **list** for frequently changing sequences.
* Use **tuple** for fixed, heterogeneous records (like coordinates), or as dictionary keys.

---

## 7.3: Modules & `pip` — Stepwise

### Step 1 — Using built-in modules

```python
import math
print(math.sqrt(16))
```

### Step 2 — Create your own module

File `mymath.py`:

```python
def add(a, b):
    return a + b
```

Import from same directory:

```python
import mymath
print(mymath.add(2,3))
```

### Step 3 — Packages (folder structure)

```
my_package/
  __init__.py
  helpers.py
  analytics/
    __init__.py
    stats.py
```

Import example: `from my_package.analytics import stats`

### Step 4 — `pip` install packages (best practices)

* Create virtual environment:

  * Windows:

    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```
  * macOS / Linux:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
* Install:

  ```bash
  pip install requests
  ```
* Save dependencies:

  ```bash
  pip freeze > requirements.txt
  ```
* To install from `requirements.txt`:

  ```bash
  pip install -r requirements.txt
  ```

### Tips

* Use `venv` for project isolation.
* Prefer pinned versions in `requirements.txt` for reproducibility.
* Use `pip show pkgname` to inspect installed package info.

---

## 7.4: File Handling — Stepwise

### Step 1 — Open/Read/Write using context manager

```python
# Write text
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")

# Read text
with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Append
with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("More text\n")
```

### Step 2 — Read line-by-line (for loops)

```python
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())
```

### Step 3 — Modes summary

* `'r'` read (default), `'w'` write (truncate), `'a'` append, `'x'` exclusive create, `'b'` binary mode, `'+'` read/write.

### Step 4 — CSV files (`csv` module)

```python
import csv

# Write CSV
rows = [["name","qty"], ["apple", 10], ["mango", 5]]
with open("stock.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# Read CSV as dicts
with open("stock.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["qty"])
```

### Step 5 — JSON (`json` module)

```python
import json
data = {"name": "Alice", "age": 30}
with open("person.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

with open("person.json", "r", encoding="utf-8") as f:
    obj = json.load(f)
```

### Step 6 — Path operations (`pathlib`)

```python
from pathlib import Path
p = Path("reports")
p.mkdir(exist_ok=True)
file = p / "report.txt"
```

### Best practices

* Always use `with` to auto-close files.
* Use `encoding="utf-8"` for portability.
* Catch exceptions only when you can handle them meaningfully.

---

## 7.5: Quiz — Functions, Dictionaries, Tuples & File Handling

**Q1.** What is returned by:

```python
def f(a, b=2):
    return a * b
print(f(3))
```

**Q2.** Which method returns all key-value pairs of a dict?
**Q3.** What is the type of `("hello",)`?
**Q4.** How would you open a file for writing (overwriting) in Python?
**Q5.** How to safely read a JSON file into a Python dict?

### ✅ Answers

* **A1:** `6` (default `b=2`).
* **A2:** `.items()`
* **A3:** `tuple` (single-element tuple needs trailing comma).
* **A4:** `open("file.txt", "w")` (prefer `with open(..., "w") as f:`).
* **A5:**

  ```python
  import json
  with open("file.json","r",encoding="utf-8") as f:
      data = json.load(f)
  ```

---

## 7.6: Mr.Beginner’s Request to Mr.Expert — Real-world Task (stepwise + solution)

**Task description (story):**
Mr.Beginner gives Mr.Expert a folder of daily sales records in CSV (each row: `product,quantity,price`). Mr.Beginner asks Mr.Expert to:

1. Compute total sales per product for the day.
2. Save a summary CSV `summary.csv` with columns `product,total_quantity,total_revenue`.

### Stepwise approach

1. Read `sales.csv` line by line (CSV reader).
2. Use a dictionary to aggregate: `{product: {"qty": int, "revenue": float}}`.
3. Write aggregated results to `summary.csv`.
4. Print a short report.

### Mr.Expert's solution (complete)

```python
import csv

# Step 1: read and aggregate
aggregates = {}   # product -> {"qty": int, "revenue": float}
with open("sales.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        qty = int(row["quantity"])
        price = float(row["price"])
        revenue = qty * price

        if product in aggregates:
            aggregates[product]["qty"] += qty
            aggregates[product]["revenue"] += revenue
        else:
            aggregates[product] = {"qty": qty, "revenue": revenue}

# Step 2: write summary.csv
with open("summary.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["product", "total_quantity", "total_revenue"])
    for product, vals in aggregates.items():
        writer.writerow([product, vals["qty"], round(vals["revenue"], 2)])

# Step 3: print report
total_day = 0
for p, v in aggregates.items():
    print(f"- {p}: {v['qty']} units, Revenue: ₹{v['revenue']:.2f}")
    total_day += v["revenue"]
print(f"Total Revenue for the day: ₹{total_day:.2f}")
```

**Notes**

* Uses `for` loops for aggregation and writing.
* Rounds revenue for readability.
* Add error handling if CSV may have malformed rows.

---

## 7.7: Exercises — Stepwise + Solutions

### Exercise 1 — Write a reusable function to filter positive numbers

**Task:** Implement `filter_positive(lst)` that returns only positive numbers.
**Solution**

```python
def filter_positive(lst):
    positives = []
    for x in lst:
        if x > 0:
            positives.append(x)
    return positives

# Example
print(filter_positive([-2, 0, 3, 5, -1]))  # [3,5]
```

---

### Exercise 2 — Word frequency from a text file

**Task:** Read `story.txt` and compute frequency of each word (case-insensitive), save top 5 to `top5.csv`.
**Solution**

```python
import csv
from collections import Counter
import re

# Read and normalize
text = ""
with open("story.txt", "r", encoding="utf-8") as f:
    for line in f:
        text += line.lower()

words = re.findall(r"\b\w+\b", text)
freq = Counter()
for w in words:
    freq[w] += 1

top5 = freq.most_common(5)

with open("top5.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["word","count"])
    for word, count in top5:
        writer.writerow([word, count])
```

---

### Exercise 3 — Create a module and import it

**Task:** Create `utils.py` with function `is_even(n)`; import and use it from `main.py`.
**Solution**
`utils.py`:

```python
def is_even(n):
    return n % 2 == 0
```

`main.py`:

```python
import utils

nums = [1,2,3,4]
evens = []
for n in nums:
    if utils.is_even(n):
        evens.append(n)
print(evens)  # [2,4]
```

---

### Exercise 4 — Save a Python object as JSON

**Task:** Convert a list of dicts to a JSON file.
**Solution**

```python
import json

data = [
    {"name": "A", "score": 90},
    {"name": "B", "score": 75}
]
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
```

---

## 7.8: Two Deadly Viruses Infecting Learners (metaphor + remedies)

Learners often get "infected" by habits that drastically slow progress. Two common ones:

### Virus 1 — **Copy-Paste Syndrome**

**Symptoms**

* Copy code from the internet and run it without understanding.
* Cannot explain what the code does.
  **Impact**
* Superficial knowledge; fragile debugging skills.
  **Cure**

1. After copying code, **read every line** and comment what it does.
2. Modify one behavior — test and observe.
3. Re-implement the logic from scratch without looking.

---

### Virus 2 — **Perfection Paralysis**

**Symptoms**

* Spending excessive time optimizing or making code "perfect" before finishing a small working version.
* Fear of committing or sharing code.
  **Impact**
* Stalled progress, demotivation, missed learning-by-doing opportunities.
  **Cure**

1. Follow **MVP (Minimum Viable Product)**: get a working solution first.
2. Timebox improvements (e.g., 30 minutes to refactor).
3. Share early — feedback accelerates learning.

> Both viruses are treatable: prefer iteration, explain your code, and practice small, frequent projects.

---

## 7.9: Thumbnail

* **Functions** are modular units of business logic — they encapsulate behaviour, improve maintainability, and enable reuse across the codebase. Adopt clear naming, concise responsibilities, and documentation to scale engineering productivity.
* **Dictionaries and tuples** are essential data structures: dictionaries offer high-performance key-based lookup for records and counters; tuples provide immutable, memory-efficient containers ideal for fixed records and hashing scenarios.
* **Modules and pip** form the backbone of Python’s ecosystem. Use virtual environments to isolate dependencies, maintain `requirements.txt` for reproducibility, and structure code into modules/packages for discoverability and reuse.
* **File handling** is fundamental for real-world data workflows — mastering text, CSV, and JSON input/output, along with safe resource management (`with` context managers) and robust error handling, is critical for production readiness.
* Avoid common learning pitfalls: do not substitute comprehension with copy-paste, and prioritize functional iterations over premature perfection. Build, test, and iterate.

---

Which would you like next?
