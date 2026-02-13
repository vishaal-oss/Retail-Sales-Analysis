import pandas as pd

# Load dataset
df = pd.read_csv("superstore.csv", encoding="latin1")

# Check original columns
print("Before Cleaning:")
print(df.columns)

# Fix encoding issue
df.columns = df.columns.str.replace('ï»¿', '', regex=False)

# Remove extra spaces
df.columns = df.columns.str.strip()

# Replace spaces with underscore
df.columns = df.columns.str.replace(' ', '_')

# Convert to lowercase (professional format)
df.columns = df.columns.str.lower()

print("\nAfter Cleaning:")
print(df.columns)
print("\nMissing Values:")
print(df.isnull().sum())
df['postal_code'] = df['postal_code'].fillna(0)
df['sales'] = df['sales'].fillna(df['sales'].median())
df['profit'] = df['profit'].fillna(df['profit'].median())
df['segment'] = df['segment'].fillna(df['segment'].mode()[0])
df['region'] = df['region'].fillna(df['region'].mode()[0])
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())
print("\nCurrent Data Types:")
print(df.dtypes)
df['order_date'] = pd.to_datetime(df['order_date'])
df['ship_date'] = pd.to_datetime(df['ship_date'])
df['sales'] = pd.to_numeric(df['sales'])
df['profit'] = pd.to_numeric(df['profit'])
df['discount'] = pd.to_numeric(df['discount'])
df['quantity'] = pd.to_numeric(df['quantity'])
df['shipping_cost'] = pd.to_numeric(df['shipping_cost'])
df['postal_code'] = df['postal_code'].astype(str)
print("\nData Types After Fixing:")
print(df.dtypes)
print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())
df['profit_margin'] = df['profit'] / df['sales']
df['delivery_days'] = (df['ship_date'] - df['order_date']).dt.days
df['year'] = df['order_date'].dt.year
df['month'] = df['order_date'].dt.month
df['month_name'] = df['order_date'].dt.month_name()
df['sales_per_unit'] = df['sales'] / df['quantity']
df.to_csv("cleaned_superstore.csv", index=False)
print("\nCleaned dataset saved successfully!")
