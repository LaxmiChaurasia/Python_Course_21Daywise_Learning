# 📊 Day10: Python Basics — Exploratory Data Analysis (EDA) Using Pandas, Matplotlib & Seaborn

## Topics Covered
- 10.1: Pandas Introduction and Installation 🐼
- 10.2: DataFrame Basics 📑
- 10.3: Read & Write Excel/CSV Files 📂
- 10.4: Handle NA Values — Part 1 ❌
- 10.5: Handle NA Values — Part 2 🔄
- 10.6: GroupBy 📊
- 10.7: Concat & Merge 🔗
- 10.8: Data Visualization Using Matplotlib & Seaborn 📈🎨
- 10.9: Quiz — EDA Using Python ❓

---

Exploratory Data Analysis (EDA) helps us **understand datasets** by cleaning, organizing, and visualizing data.
In this chapter, we will use **Pandas** for data manipulation and **Matplotlib + Seaborn** for data visualization.

---

## 10.1: Pandas Introduction and Installation 🐼

* Pandas = **Python Data Analysis Library**
* Used to work with **rows and columns (like Excel)**
* Install:

```bash
pip install pandas
```

```python
import pandas as pd
```

---

## 10.2: DataFrame Basics 📑

* **DataFrame** = Table with rows and columns
* **Series** = Single column (1D array)

```python
import pandas as pd

data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}
df = pd.DataFrame(data)

print(df)
print(df["Name"])   # Access a column
```

---

## 10.3: Read & Write Excel/CSV Files 📂

* Load datasets from files easily.

```python
# Read CSV
df = pd.read_csv("data.csv")

# Read Excel
df = pd.read_excel("data.xlsx")

# Write CSV
df.to_csv("output.csv", index=False)
```

---

## 10.4: Handle NA Values — Part 1 ❌

Missing data is common in real-world datasets.

```python
df = pd.DataFrame({
    "Name": ["Alice", "Bob", None],
    "Age": [25, None, 30]
})

print(df.isnull())         # Check NA values
print(df.dropna())         # Drop rows with NA
```

---

## 10.5: Handle NA Values — Part 2 🔄

Replace missing values with defaults.

```python
df.fillna({"Name": "Unknown", "Age": df["Age"].mean()}, inplace=True)
print(df)
```

---

## 10.6: GroupBy 📊

Group data and calculate statistics.

```python
data = {
    "Department": ["HR", "HR", "IT", "IT", "Finance"],
    "Salary": [3000, 3200, 4000, 4200, 5000]
}
df = pd.DataFrame(data)

print(df.groupby("Department")["Salary"].mean())
```

---

## 10.7: Concat & Merge 🔗

* **Concat:** Combine rows/columns
* **Merge:** Join tables (like SQL)

```python
# Concat
df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})
print(pd.concat([df1, df2]))

# Merge
emp = pd.DataFrame({"ID": [1, 2], "Name": ["Alice", "Bob"]})
sal = pd.DataFrame({"ID": [1, 2], "Salary": [3000, 4000]})
print(pd.merge(emp, sal, on="ID"))
```

---

## 10.8: Data Visualization Using Matplotlib & Seaborn 📈🎨

### Matplotlib Example:

```python
import matplotlib.pyplot as plt

df["Age"].plot(kind="hist", bins=5, title="Age Distribution")
plt.show()
```

### Seaborn Example:

```python
import seaborn as sns

sns.barplot(x="Department", y="Salary", data=df)
plt.show()
```

---

## 10.9: Quiz — EDA Using Python ❓

**Q1.** What is the difference between `concat` and `merge`?
**Q2.** How do you fill missing values with the mean in Pandas?
**Q3.** Which library is better for statistical plots: Matplotlib or Seaborn?

---

## ✅ Thumbnail 📘

* **Pandas** → Handle structured data (tables).
* **Read/Write CSV & Excel** files easily.
* **Handle NA values** with drop or fill methods.
* **GroupBy, Merge, Concat** → Powerful data operations.
* **Matplotlib + Seaborn** → Create clear and beautiful visualizations.

🚀 With Pandas, Matplotlib, and Seaborn, you can perform **complete EDA workflows** for any dataset.

---

Would you like me to also create a **mini-project for this chapter (like analyzing sales data step-by-step)** so your GitHub repo has both **theory + real-life project**?
