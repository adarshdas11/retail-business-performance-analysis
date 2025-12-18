import pandas as pd

# Load dataset
df = pd.read_csv("../data/superstore.csv", encoding="latin1")


# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Display column names
print("\nColumns:")
print(df.columns)

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nData types:")
print(df.dtypes)

# Convert date columns to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print("\nUpdated data types after date conversion:")
print(df.dtypes)


# Sales and Profit by Category
category_summary = (
    df.groupby("Category")[["Sales", "Profit"]]
      .sum()
      .sort_values(by="Profit", ascending=False)
)

print("\nSales and Profit by Category:")
print(category_summary)


# Profit by Sub-Category
subcat_summary = (
    df.groupby("Sub-Category")[["Sales", "Profit"]]
      .sum()
      .sort_values(by="Profit")
)

print("\nSales and Profit by Sub-Category:")
print(subcat_summary)

# Create Year-Month column
df["YearMonth"] = df["Order Date"].dt.to_period("M")

monthly_summary = (
    df.groupby("YearMonth")[["Sales", "Profit"]]
      .sum()
)

print("\nMonthly Sales and Profit:")
print(monthly_summary.head(12))


# Export cleaned data for Tableau
df.to_csv("../tableau/retail_cleaned_data.csv", index=False)
print("\nCleaned data exported for Tableau.")
