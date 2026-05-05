import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the data
df = pd.read_excel("monthly_sales.xlsx")  # Replace with the correct file path if needed

# Step 2: Group by item to compute total revenue and unit price
grouped = df.groupby("Item").agg({
    "Revenue": "sum",
    "Sales Price": "first"  # Assuming each product has a fixed unit price
}).reset_index()

# Step 3: Calculate revenue-to-price ratio
grouped["Revenue-to-Price Ratio"] = grouped["Revenue"] / grouped["Sales Price"]

# Step 4: Sort and get top 10
top_ratio = grouped.sort_values(by="Revenue-to-Price Ratio", ascending=False).head(10)

# Step 5: Plot the bar chart
plt.figure(figsize=(12, 6))
plt.bar(top_ratio["Item"], top_ratio["Revenue-to-Price Ratio"], color='teal')
plt.xticks(rotation=45, ha='right')
plt.ylabel("Revenue-to-Price Ratio")
plt.title("Top 10 Products by Revenue-to-Price Ratio (November 2024)")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
