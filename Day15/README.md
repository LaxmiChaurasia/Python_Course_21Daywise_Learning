# Day15: Python Advanced — Logging, Pytest, Pydantic, and Databases**

## Topics Covered
- 15.1 Logging
- 15.2 Automated Testing with Pytest
- 15.3 MySQL Setup: Windows
- 15.4 MySQL Setup: Linux, Mac
- 15.5 Working with MySQL in Python
- 15.6 Data Validation with Pydantic
- 15.7 Quiz: Logging, Pytest, Pydantic and Databases
- 15.8 Exercises: Pytest, Pydantic
- 15.9 Chapter Summary


---

# 🗄️ Python Advanced: Logging, Pytest, Pydantic and Databases

In this chapter, we focus on **production-level coding practices**: logging for debugging, automated testing with Pytest, connecting Python with MySQL, and validating data with Pydantic.

---

## 📖 15.1 Logging

* Logging helps to **track events** when software runs.
* Useful for debugging and monitoring applications.

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("This is an info message")
logging.warning("This is a warning")
logging.error("This is an error")
```

---

## 🧪 15.2 Automated Testing with Pytest

* Pytest is a **testing framework** in Python.
* Helps in writing unit tests.

**Installation:**

```bash
pip install pytest
```

**Example:**
Create a file `test_calc.py`:

```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```

Run tests:

```bash
pytest
```

---

## 🖥️ 15.3 MySQL Setup: Windows

* Download and install MySQL Community Server.
* Install MySQL Workbench for GUI.
* Set a root password and remember it.

---

## 💻 15.4 MySQL Setup: Linux, Mac

* Install using package manager:

```bash
# Ubuntu / Debian
sudo apt-get install mysql-server

# Mac
brew install mysql
```

* Start the MySQL service:

```bash
sudo service mysql start
```

---

## 🔗 15.5 Working with MySQL in Python

Install MySQL connector:

```bash
pip install mysql-connector-python
```

**Example:**

```python
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="testdb"
)

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
conn.commit()

cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

conn.close()
```

---

## ✅ 15.6 Data Validation with Pydantic

* Pydantic helps to **validate and parse data**.
* Used in FastAPI and modern projects.

**Installation:**

```bash
pip install pydantic
```

**Example:**

```python
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int
    name: str
    email: EmailStr

user = User(id=1, name="John Doe", email="john@example.com")
print(user)
```

---

## 📝 15.7 Quiz: Logging, Pytest, Pydantic and Databases

1. Which module is used for logging in Python?
2. How do you run Pytest from terminal?
3. What is the purpose of Pydantic?
4. Which Python package is used for MySQL connection?

---

## 💻 15.8 Exercises: Pytest, Pydantic

1. Write a Pytest function to test subtraction.
2. Use Pydantic to validate a student model with `id`, `name`, `age`.
3. Connect to MySQL, create a `products` table, and insert sample records.

---

## 📌 15.9 Chapter Summary

* **Logging** → Tracks events & helps debug.
* **Pytest** → Automates testing process.
* **MySQL** → Store & manage relational data.
* **Pydantic** → Validates and parses structured data.

🚀 With these tools, your Python code becomes **robust, testable, and production-ready**.

---

✨ This makes your repo look **professional & practical** with code snippets, quizzes, and exercises.

Do you want me to also **generate a Jupyter Notebook (.ipynb)** version (like we did for APIs) so learners can run everything step by step?

