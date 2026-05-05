import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load data
df = pd.read_excel("monthly_sales.xlsx")

# Step 2: Group by Item and sum Units Sold
product_sales = df.groupby('Item')['Units Sold'].sum().sort_values(ascending=False)

# Step 3: Keep top 20 products (you can change the number if needed)
top_products = product_sales.head(20)

# Step 4: Calculate cumulative percent
cumulative_percent = top_products.cumsum() / top_products.sum() * 100

# Step 5: Plot Pareto chart
fig, ax = plt.subplots(figsize=(12, 6))

# Bar chart for units sold
bars = ax.bar(top_products.index, top_products.values, color='skyblue')
ax.set_ylabel('Units Sold')
ax.set_xticklabels(top_products.index, rotation=45, ha='right')

# Line plot for cumulative %
ax2 = ax.twinx()
ax2.plot(top_products.index, cumulative_percent.values, color='red', marker='o', linestyle='-')
ax2.set_ylabel('Cumulative % of Units Sold')
ax2.set_ylim(0, 110)  # extend y-axis to 110% for clarity

# Add grid only to primary y-axis
ax.grid(True, axis='y', linestyle='--', alpha=0.7)

# Title and layout
plt.title('Pareto Chart for Top 20 Products by Units Sold')
plt.tight_layout()
plt.show()
