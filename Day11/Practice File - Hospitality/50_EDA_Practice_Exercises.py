"""
50_EDA_Practice_Exercises.py

50 practice exercises (with solutions) for Exploratory Data Analysis (EDA)
on the hospitality dummy dataset containing:
 - dim_hotels.csv
 - dim_customers.csv
 - dim_rooms.csv
 - fact_bookings.csv

Usage:
 - Place this script under `scripts/` folder in your repo and the CSV files in `data/` folder.
 - Run in Jupyter or as a script. Cells/comments are structured for easy conversion to a notebook.

Note: The script will try to locate the CSV files under ../data/ and ./data/ automatically.
"""

# === Imports ===
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import sys

plt.rcParams.update({'figure.max_open_warning': 0})

# === Helper: locate data files (search ../data, ./data, /mnt/data) ===
def find_data_path():
    candidates = [Path("../data"), Path("./data"), Path("/mnt/data"), Path(".")]
    for c in candidates:
        if (c / "dim_hotels.csv").exists():
            return c
    raise FileNotFoundError("Could not find dim_hotels.csv in ../data, ./data, /mnt/data, or current directory. Put CSVs in a data/ folder.")

DATA_DIR = find_data_path()
print("Using data from:", DATA_DIR.resolve())

# === Load datasets ===
hotels = pd.read_csv(DATA_DIR / "dim_hotels.csv")
customers = pd.read_csv(DATA_DIR / "dim_customers.csv")
rooms = pd.read_csv(DATA_DIR / "dim_rooms.csv")
bookings = pd.read_csv(DATA_DIR / "fact_bookings.csv")

# Ensure datetime types
if 'check_in' in bookings.columns:
    bookings['check_in'] = pd.to_datetime(bookings['check_in'])
if 'check_out' in bookings.columns:
    bookings['check_out'] = pd.to_datetime(bookings['check_out'])

# Merge helper
def merge_all(bookings_df=bookings):
    df = bookings_df.merge(hotels, on="hotel_id", how="left").merge(customers, on="customer_id", how="left").merge(rooms, on="room_id", how="left")
    return df

# Pre-calc price_per_night presence: if missing in bookings, take from rooms
if 'price_per_night' not in bookings.columns and 'price_per_night' in rooms.columns:
    bookings = bookings.merge(rooms[['room_id','price_per_night']], on='room_id', how='left')

# Add computed fields for convenience
bookings['nights'] = bookings['nights'].astype(int)
bookings['total_revenue'] = bookings['nights'] * bookings['price_per_night']

# ----------------------------------------------------------------------------
# Exercises 1-50: Each exercise is shown as a short task followed by solution code
# ----------------------------------------------------------------------------

# Exercise 1: Show basic row/column counts for each file
print("\\nExercise 1: Dataset shapes")
print("hotels:", hotels.shape)
print("customers:", customers.shape)
print("rooms:", rooms.shape)
print("bookings:", bookings.shape)

# Exercise 2: Show first 3 rows of each dataset
print("\\nExercise 2: First 3 rows (hotels/customers/rooms/bookings)")
print(hotels.head(3).to_string(index=False))
print(customers.head(3).to_string(index=False))
print(rooms.head(3).to_string(index=False))
print(bookings.head(3).to_string(index=False))

# Exercise 3: Count unique hotels, customers, room types
print("\\nExercise 3: Unique counts")
print("unique hotels:", hotels['hotel_id'].nunique())
print("unique customers:", customers['customer_id'].nunique())
print("unique room types:", rooms['room_type'].nunique())

# Exercise 4: Check missing values in bookings
print("\\nExercise 4: Missing values in bookings")
print(bookings.isnull().sum())

# Exercise 5: Top 5 hotels by number of bookings
print("\\nExercise 5: Top 5 hotels by booking count")
top_hotels = bookings['hotel_id'].value_counts().head(5).rename_axis('hotel_id').reset_index(name='counts')
top_hotels = top_hotels.merge(hotels, on='hotel_id', how='left')
print(top_hotels[['hotel_id','hotel_name','counts']])

# Exercise 6: Total revenue per hotel (descending)
print("\\nExercise 6: Total revenue per hotel")
rev_per_hotel = bookings.groupby('hotel_id')['total_revenue'].sum().reset_index().merge(hotels, on='hotel_id', how='left').sort_values('total_revenue', ascending=False)
print(rev_per_hotel[['hotel_id','hotel_name','total_revenue']].head(10).to_string(index=False))

# Exercise 7: Average nights per booking
print("\\nExercise 7: Average nights per booking:", bookings['nights'].mean())

# Exercise 8: Revenue per room type (join rooms)
print("\\nExercise 8: Revenue per room type")
rev_room = bookings.merge(rooms, on='room_id', how='left').groupby('room_type')['total_revenue'].sum().reset_index().sort_values('total_revenue', ascending=False)
print(rev_room.to_string(index=False))

# Exercise 9: Most frequent customer (by number of bookings)
print("\\nExercise 9: Most frequent customers")
top_customers = bookings['customer_id'].value_counts().head(5).rename_axis('customer_id').reset_index(name='bookings_count').merge(customers, on='customer_id', how='left')
print(top_customers[['customer_id','customer_name','bookings_count']])

# Exercise 10: Distribution of rating for hotels
print("\\nExercise 10: Hotel ratings distribution")
print(hotels['rating'].describe())
try:
    hotels['rating'].hist()
    plt.title("Hotel Rating Distribution")
    plt.show()
except Exception as e:
    print("Plotting unavailable in this environment:", e)

# Exercise 11: Add length_of_stay if not present
print("\\nExercise 11: Add length_of_stay (days)")
if 'length_of_stay' not in bookings.columns:
    bookings['length_of_stay'] = (bookings['check_out'] - bookings['check_in']).dt.days
print(bookings[['booking_id','check_in','check_out','length_of_stay']].head())

# Exercise 12: Booking trend by month (counts)
print("\\nExercise 12: Monthly booking counts")
monthly_counts = bookings.groupby(bookings['check_in'].dt.to_period('M'))['booking_id'].count().sort_index()
print(monthly_counts)

# Exercise 13: Peak booking month
print("\\nExercise 13: Peak booking month")
print(monthly_counts.idxmax(), monthly_counts.max())

# Exercise 14: Customers by city (top 5)
print("\\nExercise 14: Customers by city")
print(customers['city'].value_counts().head(10))

# Exercise 15: Average revenue per booking
print("\\nExercise 15: Average revenue per booking:", bookings['total_revenue'].mean())

# Exercise 16: Percentage of bookings per room type
print("\\nExercise 16: Percentage bookings by room type")
room_counts = bookings['room_id'].map(rooms.set_index('room_id')['room_type']).value_counts(normalize=True) * 100
print(room_counts.round(2))

# Exercise 17: Correlation between nights and revenue
print("\\nExercise 17: Correlation nights vs revenue:", bookings['nights'].corr(bookings['total_revenue']))

# Exercise 18: Create merged dataframe (bookings + hotels + customers + rooms)
print("\\nExercise 18: Create merged dataframe (merged_df)")
merged_df = merge_all()
print(merged_df.head(3).to_string(index=False))

# Exercise 19: Top 5 revenue generating customers
print("\\nExercise 19: Top 5 customers by revenue")
cust_rev = merged_df.groupby(['customer_id','customer_name'])['total_revenue'].sum().reset_index().sort_values('total_revenue',ascending=False).head(5)
print(cust_rev.to_string(index=False))

# Exercise 20: Bookings with check_in weekend (Sat/Sun)
print("\\nExercise 20: Weekend bookings")
bookings['weekday'] = bookings['check_in'].dt.weekday  # Monday=0
weekend = bookings[bookings['weekday'] >=5]
print("Weekend count:", len(weekend))

# Exercise 21: Find bookings longer than 7 nights
print("\\nExercise 21: Bookings longer than 7 nights")
long_stays = bookings[bookings['nights'] > 7]
print(long_stays[['booking_id','nights']].head())

# Exercise 22: Count repeat customers (customers with >1 booking)
print("\\nExercise 22: Repeat customers count")
rep = bookings['customer_id'].value_counts()
print((rep>1).sum(), "customers have more than 1 booking")

# Exercise 23: Room utilization rate (booked nights / possible nights sample)
print("\\nExercise 23: Simple room utilization approximation by room type")
# approximation: total nights for room type / (number of rooms * period days) - but we don't have room inventory counts; show total nights per room type
nights_by_room = bookings.merge(rooms,on='room_id').groupby('room_type')['nights'].sum().reset_index()
print(nights_by_room.to_string(index=False))

# Exercise 24: Most common check-in month
print("\\nExercise 24: Most common check-in month")
print(bookings['check_in'].dt.month.mode())

# Exercise 25: Average age of customers
print("\\nExercise 25: Average customer age:", customers['age'].mean())

# Exercise 26: Gender distribution of customers
print("\\nExercise 26: Gender distribution")
print(customers['gender'].value_counts(normalize=True) * 100)

# Exercise 27: Simple pivot: bookings count by hotel and room_type
print("\\nExercise 27: Pivot bookings by hotel_name and room_type (counts)")
pivot = merge_all().pivot_table(index='hotel_name', columns='room_type', values='booking_id', aggfunc='count', fill_value=0)
print(pivot.head())

# Exercise 28: Create column 'revenue_per_night' (should equal price_per_night)
print("\\nExercise 28: revenue_per_night check")
merged_df['revenue_per_night'] = merged_df['total_revenue'] / merged_df['nights']
print(merged_df[['booking_id','revenue_per_night','price_per_night']].head())

# Exercise 29: Find bookings where price seems missing (NaN)
print("\\nExercise 29: Bookings with missing price_per_night")
print(bookings[bookings['price_per_night'].isnull()].head())

# Exercise 30: Histogram of total_revenue
print("\\nExercise 30: Histogram of total_revenue (sample)")
try:
    bookings['total_revenue'].hist(bins=20)
    plt.title("Total Revenue Histogram")
    plt.show()
except Exception as e:
    print("Plotting unavailable:", e)

# Exercise 31: Top 5 booking days (date) by bookings count
print("\\nExercise 31: Top 5 check-in dates by bookings")
top_days = bookings['check_in'].dt.date.value_counts().head(5)
print(top_days)

# Exercise 32: Average nights by room type
print("\\nExercise 32: Average nights by room type")
avg_nights_room = merged_df.groupby('room_type')['nights'].mean().reset_index().sort_values('nights', ascending=False)
print(avg_nights_room.to_string(index=False))

# Exercise 33: Percentage revenue contribution by hotel
print("\\nExercise 33: Revenue contribution by hotel (%)")
rev = merged_df.groupby('hotel_name')['total_revenue'].sum()
print((rev / rev.sum() * 100).round(2).sort_values(ascending=False))

# Exercise 34: Find customers who visited more than 2 unique hotels
print("\\nExercise 34: Customers who visited >2 unique hotels")
cust_hotels = bookings.groupby('customer_id')['hotel_id'].nunique().reset_index()
multi_hot = cust_hotels[cust_hotels['hotel_id']>2].merge(customers,on='customer_id', how='left')
print(multi_hot.head())

# Exercise 35: Create a simple time-series of daily bookings count
print("\\nExercise 35: Daily bookings count (first 10 days)")
daily = bookings.set_index('check_in').resample('D')['booking_id'].count().fillna(0)
print(daily.head(10))

# Exercise 36: Merge bookings with customer city to analyze revenue by customer city
print("\\nExercise 36: Revenue by customer city")
rev_by_city = merge_all().groupby('city_x')['total_revenue'].sum().reset_index().rename(columns={'city_x':'hotel_city'})
print(rev_by_city.head())

# Exercise 37: Top 3 room types by revenue
print("\\nExercise 37: Top 3 room types by revenue")
print(rev_room.sort_values('total_revenue', ascending=False).head(3))

# Exercise 38: Average revenue per hotel rating (if rating exists)
if 'rating' in hotels.columns:
    print("\\nExercise 38: Average revenue per hotel rating")
    r = merge_all().groupby('rating')['total_revenue'].mean().reset_index().sort_values('rating')
    print(r)

# Exercise 39: Create a column 'is_weekend_stay' True/False
print("\\nExercise 39: is_weekend_stay column")
merged_df['is_weekend_stay'] = merged_df['weekday'] >=5
print(merged_df[['booking_id','check_in','weekday','is_weekend_stay']].head())

# Exercise 40: Simple cancellation analysis — if booking_status exists
print("\\nExercise 40: Cancellation analysis (if booking_status exists)")
if 'booking_status' in bookings.columns:
    print(bookings['booking_status'].value_counts())
else:
    print("No booking_status column in dataset; skip this exercise.")

# Exercise 41: Find earliest and latest check-in date
print("\\nExercise 41: Earliest & Latest check-in")
print(bookings['check_in'].min(), bookings['check_in'].max())

# Exercise 42: Calculate median revenue by hotel
print("\\nExercise 42: Median revenue by hotel")
print(merged_df.groupby('hotel_name')['total_revenue'].median().sort_values(ascending=False).head())

# Exercise 43: Create sample customer cohorts by first booking month
print("\\nExercise 43: Customer cohort (first booking month)")
first_booking = bookings.groupby('customer_id')['check_in'].min().reset_index()
first_booking['cohort_month'] = first_booking['check_in'].dt.to_period('M')
print(first_booking.head())

# Exercise 44: Show top 5 customers by average booking value
print("\\nExercise 44: Top customers by avg booking value")
avg_booking = merged_df.groupby(['customer_id','customer_name'])['total_revenue'].mean().reset_index().sort_values('total_revenue', ascending=False).head(5)
print(avg_booking.to_string(index=False))

# Exercise 45: Create feature 'price_category' based on price_per_night
print("\\nExercise 45: price_category feature creation")
def price_cat(p):
    if p < 2000: return 'budget'
    if p < 5000: return 'standard'
    if p < 10000: return 'premium'
    return 'luxury'
merged_df['price_category'] = merged_df['price_per_night'].apply(price_cat)
print(merged_df[['booking_id','price_per_night','price_category']].head())

# Exercise 46: Crosstab of price_category vs room_type
print("\\nExercise 46: Crosstab price_category vs room_type")
print(pd.crosstab(merged_df['price_category'], merged_df['room_type']))

# Exercise 47: Simple moving average of daily bookings (window=7)
print("\\nExercise 47: 7-day moving average of daily bookings")
daily = bookings.set_index('check_in').resample('D')['booking_id'].count().fillna(0)
ma7 = daily.rolling(7, min_periods=1).mean()
print(ma7.head(14))

# Exercise 48: Export a small report CSV (top 10 hotels by revenue)
print("\\nExercise 48: Export top 10 hotels by revenue to CSV (saved to current directory)")
top10 = rev_per_hotel[['hotel_id','hotel_name','total_revenue']].head(10)
top10.to_csv("top10_hotels_by_revenue.csv", index=False)
print("Saved top10_hotels_by_revenue.csv")

# Exercise 49: Create a simple seaborn barplot for revenue by room_type
print("\\nExercise 49: Seaborn barplot for revenue by room_type (displaying if possible)")
try:
    import matplotlib.pyplot as plt
    plt.figure(figsize=(8,4))
    sns.barplot(data=merged_df, x='room_type', y='total_revenue', estimator=sum, ci=None)
    plt.title("Revenue by Room Type")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
except Exception as e:
    print("Plotting not available in this environment:", e)

# Exercise 50: Short summary — top 3 insights (print them)
print("\\nExercise 50: Top 3 quick insights (auto-generated sample)")
insight1 = f"Top hotel by revenue: {rev_per_hotel.iloc[0]['hotel_name']} ({rev_per_hotel.iloc[0]['total_revenue']:.2f})"
insight2 = f"Most booked room type: {rev_room.iloc[0]['room_type']}"
insight3 = f"Average nights per booking: {bookings['nights'].mean():.2f}"
print(insight1)
print(insight2)
print(insight3)

# End of exercises
print("\\nAll 50 exercises completed (script run).")
