# Day14: Python Advanced: APIs**

## Topics Covered
- 14.1 What is API?
- 14.2 Calling APIs With `requests` Package
- 14.3 Building APIs With FastAPI
- 14.4 Quiz: APIs
- 14.5 Peter fetches data using APIs
- 14.6 Exercise: APIs
- 14.7 Chapter Summary


---

# 🌐 Python Advanced: APIs

In this chapter, we explore **APIs (Application Programming Interfaces)** – how to **consume APIs** using Python and how to **build APIs** using FastAPI.

---

## 📖 14.1 What is API?

* **API (Application Programming Interface)** allows communication between two applications.
* Example: Your mobile weather app calls a **Weather API** to fetch live temperature.
* APIs usually return data in **JSON format**.

---

## ⚡ 14.2 Calling APIs With `requests` Package

We can fetch API data using the `requests` library in Python.

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Title:", data["title"])
else:
    print("Error:", response.status_code)
```

✅ Output will show the **title** of a dummy blog post.

---

## 🚀 14.3 Building APIs With FastAPI

FastAPI is a modern, fast Python framework to **create APIs**.

**Install FastAPI + Uvicorn**

```bash
pip install fastapi uvicorn
```

**Basic API Example**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my API!"}

@app.get("/square/{num}")
def square(num: int):
    return {"number": num, "square": num * num}
```

Run with:

```bash
uvicorn main:app --reload
```

Open in browser:
👉 `http://127.0.0.1:8000/square/5` → `{ "number": 5, "square": 25 }`

---

## 📝 14.4 Quiz: APIs

1. What is the main purpose of an API?
2. Which Python package is commonly used to **call APIs**?
3. Which framework is used to **build APIs** in Python?

---

## 📊 14.5 Peter fetches data using APIs

Imagine Peter wants stock prices. He uses `requests` to call a **Stock Market API** and prints the result.

```python
import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url).json()

print("Bitcoin Price (USD):", response["bpi"]["USD"]["rate"])
```

---

## 💻 14.6 Exercise: APIs

1. Fetch current weather data for your city using the **OpenWeather API**.
2. Create a FastAPI route that returns multiplication of two numbers.
3. Call a public API (like JSONPlaceholder) and print **first 5 posts**.

---

## 📌 14.7 Chapter Summary

✔ APIs connect different applications.
✔ `requests` → used for fetching API data.
✔ FastAPI → used for building APIs.
✔ Real-world applications: weather apps, payment gateways, stock trackers, chatbots.
