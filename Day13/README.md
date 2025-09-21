# Day13: ⚡ Python Advanced: JSON, Generators & Decorators


## Topics Covered
- 13.1 📦 Working with JSON
- 13.2 🔄 Generators and Iterators
- 13.3 🎨 Decorators
- 13.4 📝 Quiz: JSON, Generators, and Decorators
- 13.5 💻 Exercise: JSON, Generators, and Decorators
- 13.6 📌 Chapter Summary

---

# ⚡ Python Advanced: JSON, Generators & Decorators

This chapter covers three powerful Python concepts: **JSON handling, Generators, and Decorators**. These tools help us work with data, optimize performance, and write cleaner code.

---

## 13.1 📦 Working with JSON

**JSON (JavaScript Object Notation)** is a common format for storing and exchanging data (like API responses).

### ✅ Example: Converting Python ↔ JSON

```python
import json  

# Python dictionary
student = {"name": "Alice", "age": 22, "marks": [85, 90, 95]}  

# Convert Python → JSON
json_string = json.dumps(student)  
print(json_string)  

# Convert JSON → Python
python_dict = json.loads(json_string)  
print(python_dict["name"])  
```

---

## 13.2 🔄 Generators and Iterators

* **Iterators**: Objects that can be looped over.
* **Generators**: Special functions using `yield`, which produce values one at a time (memory efficient).

### ✅ Example: Generator

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for number in countdown(5):
    print(number)
```

---

## 13.3 🎨 Decorators

**Decorators** allow you to add functionality to existing functions without changing their code.

### ✅ Example: Logging Decorator

```python
def log_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@log_decorator
def greet():
    print("Hello, Python!")

greet()
```

---

## 13.4 📝 Quiz: JSON, Generators, and Decorators

* Q1: What function converts Python objects to JSON?
* Q2: What keyword is used inside a generator?
* Q3: Why do we use decorators?

---

## 13.5 💻 Exercise: JSON, Generators, and Decorators

* Convert a list of employees into JSON format.
* Write a generator that yields even numbers up to 20.
* Create a decorator that measures the execution time of a function.

---

## 13.6 📌 Chapter Summary

✔ **JSON** → For data storage & APIs
✔ **Generators** → Memory-efficient iteration
✔ **Decorators** → Add extra functionality without modifying code

---

Would you like me to **also generate the `.ipynb` Jupyter Notebook file** (with explanations + exercises) for direct upload to GitHub?

