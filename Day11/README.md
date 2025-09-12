# 🏨 Day11: Project 1 — Exploratory Data Analytics (EDA) in Hospitality Domain


## Topics Covered
- 11.1: Problem Statement & Key Concepts 📝
- 11.2: Data Understanding — CSV Files 📂
- 11.3: Fact vs Dim Tables & Schema Design 🏗️
- 11.4: Data Exploration 🔎
- 11.5: Data Cleaning 🧹
- 11.6: Data Transformation 🔄
- 11.7: Insights Generation 📊
---

In this project, we will apply **EDA techniques** to a dataset from the **Hospitality Industry** (e.g., hotel bookings, guest records, revenue data).
You’ll learn how to **understand, clean, transform, and analyze data** to generate meaningful insights.

---

## 11.1: Problem Statement & Key Concepts 📝

**Problem Statement:**
A hotel chain wants to analyze guest booking and stay data to improve revenue, customer experience, and operations.

Before solving, we need some basics:

* **OLTP (Online Transaction Processing):**

  * Handles real-time transactions (e.g., hotel booking system).
  * Data is detailed and normalized.

* **OLAP (Online Analytical Processing):**

  * Used for analysis & reporting (e.g., guest trends, revenue patterns).
  * Data is summarized and optimized for queries.

* **ETL (Extract, Transform, Load):**

  * **Extract:** Take data from OLTP systems.
  * **Transform:** Clean and shape the data.
  * **Load:** Store in a Data Warehouse.

* **Data Warehouse:**

  * Central storage for analysis.
  * Supports **fact tables** (measurable data) and **dimension tables** (descriptive data).

---

## 11.2: Data Understanding — CSV Files 📂

We start with **CSV files** (commonly shared by businesses):

* `dim_hotels.csv` → Hotel details
* `dim_customers.csv` → Customer details
* `dim_rooms.csv` → Room categories
* `fact_bookings.csv` → Booking transactions

```python
import pandas as pd

hotels = pd.read_csv("dim_hotels.csv")
customers = pd.read_csv("dim_customers.csv")
rooms = pd.read_csv("dim_rooms.csv")
bookings = pd.read_csv("fact_bookings.csv")

print(hotels.head())
print(bookings.info())
```

---

## 11.3: Fact vs Dim Tables & Schema Design 🏗️

* **Fact Table:** Contains measurable events (e.g., bookings, revenue).
* **Dimension Tables:** Describe context (e.g., hotel name, customer details, room type).

**Schemas:**

* **Star Schema:** Fact table linked directly to dimensions.
* **Snowflake Schema:** Dimension tables are normalized further.

```plaintext
   Fact_Bookings
       |
 ┌─────────────┐
 | dim_hotels  |
 | dim_rooms   |
 | dim_customers |
 └─────────────┘
```

---

## 11.4: Data Exploration 🔎

* Explore shape, columns, summary stats
* Check missing values

```python
print(bookings.describe())
print(bookings['booking_status'].value_counts())
print(customers['country'].unique())
```

---

## 11.5: Data Cleaning 🧹

Steps:

1. Handle missing values (`dropna`, `fillna`)
2. Correct data types (e.g., `date` columns)
3. Remove duplicates

```python
bookings['check_in'] = pd.to_datetime(bookings['check_in'])
bookings.drop_duplicates(inplace=True)
```

---

## 11.6: Data Transformation 🔄

* Add calculated fields (e.g., length of stay, total revenue).
* Merge fact and dimension tables.

```python
bookings['stay_length'] = (bookings['check_out'] - bookings['check_in']).dt.days
bookings['total_revenue'] = bookings['nights'] * bookings['price_per_night']

merged = bookings.merge(hotels, on="hotel_id").merge(customers, on="customer_id")
```

---

## 11.7: Insights Generation 📊

Examples of business insights:

1. **Revenue Insights:**

   * Which hotel generates the most revenue?
   * Average revenue per customer.

2. **Customer Insights:**

   * Most common guest nationality.
   * Repeat guest percentage.

3. **Operational Insights:**

   * Average length of stay.
   * Most popular room type.

```python
print(merged.groupby("hotel_name")["total_revenue"].sum())
print(merged.groupby("country")["customer_id"].count().sort_values(ascending=False))
```

📈 You can visualize these using **Matplotlib/Seaborn** for better insights.

---

## ✅ Project Summary

* Learned **OLTP vs OLAP, ETL, and Data Warehouse concepts**.
* Explored **fact and dimension tables**.
* Cleaned & transformed hospitality data.
* Generated **actionable insights** for hotel management.

🚀 This project shows how **EDA helps businesses** make better decisions using data.

---
