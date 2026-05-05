import pandas as pd
import matplotlib.pyplot as plt

# Load your monthly sales data
df = pd.read_excel("monthly_sales.xlsx")  # Replace with your actual file path if needed

# Group by Item and sum total revenue
top_products_by_revenue = df.groupby('Item')['Revenue'].sum().sort_values(ascending=False).head(10)

# Plot bar chart
plt.figure(figsize=(12, 6))
plt.bar(top_products_by_revenue.index, top_products_by_revenue.values, color='orange')
plt.xticks(rotation=45, ha='right')
plt.ylabel("Total Revenue (₹)")
plt.title("Top 10 Products by Monthly Revenue")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
