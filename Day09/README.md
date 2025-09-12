# Day09: Python Basics — NumPy📊 

## Topics Covered
- 9.1: Introduction and Benefits 🌟
- 9.2: Basic Operations 🔢
- 9.3: Matrix Operations 🧮
- 9.4: Slicing & Stacking ✂️📚
- 9.5: Quiz — NumPy ❓
- 9.6: Mr. Beginner Solves a Real-Time Problem 💡
- 9.7: Exercise — NumPy 📝
- 9.8: Thumbnail 📘

---



NumPy is one of the most powerful libraries in Python.
It is used for **fast mathematical operations, arrays, and data science tasks**.

---

## 9.1: Introduction and Benefits 🌟

* NumPy = **Numerical Python**
* Works faster than normal Python lists
* Used in **Data Science, Machine Learning, AI, Finance, Engineering**
* Benefits:

  * Fast mathematical operations
  * Multi-dimensional arrays
  * Easy integration with Pandas, Matplotlib, Scikit-learn

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", arr)
```

---

## 9.2: Basic Operations 🔢

With NumPy, you can do **element-wise operations** easily.

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)   # [5 7 9]
print(a * b)   # [4 10 18]
print(a ** 2)  # [1 4 9]
```

✅ Much faster than using Python loops!

---

## 9.3: Matrix Operations 🧮

NumPy can handle **2D arrays (matrices)** easily.

```python
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

print(matrix1 + matrix2)        # Matrix addition
print(matrix1 @ matrix2)        # Matrix multiplication
print(np.transpose(matrix1))    # Transpose
```

---

## 9.4: Slicing & Stacking ✂️📚

* **Slicing:** Extract part of an array
* **Stacking:** Combine arrays vertically or horizontally

```python
arr = np.array([10, 20, 30, 40, 50])
print(arr[1:4])   # [20 30 40]

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

print(np.vstack((a, b)))  # Vertical stack
print(np.hstack((a, b.T)))  # Horizontal stack
```

---

## 9.5: Quiz — NumPy ❓

**Q1.** Which is faster, NumPy arrays or Python lists?
**Q2.** What does `@` operator do in NumPy?
**Q3.** If `arr = np.array([10, 20, 30, 40])`, what is `arr[1:3]`?

---

## 9.6: Mr. Beginner Solves a Real-Time Problem 💡

👉 Problem: A shopkeeper wants to calculate the **total revenue** from daily sales of 5 products quickly.

```python
prices = np.array([20, 35, 12, 50, 25])
quantities = np.array([15, 10, 20, 5, 8])

revenue = prices * quantities
print("Revenue per product:", revenue)
print("Total Revenue:", revenue.sum())
```

✅ NumPy makes real-world calculations **super fast & easy**!

---

## 9.7: Exercise — NumPy 📝

1. Create a NumPy array `[5, 10, 15, 20, 25]` and find its square.
2. Create a 2x3 matrix and calculate its transpose.
3. Stack two arrays horizontally and vertically.

---

## 9.8: Thumbnail 📘

* NumPy = **Numerical Python**, optimized for speed.
* Handles arrays and matrices efficiently.
* Supports slicing, stacking, and complex mathematical operations.
* Real-world problems like finance, engineering, AI rely on NumPy.

✅ Mastering NumPy is the **first big step** towards Data Science & Machine Learning. 🚀

---
