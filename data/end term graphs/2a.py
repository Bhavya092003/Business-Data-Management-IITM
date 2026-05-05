import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_excel("monthly_sales.xlsx")

# Group and sum units sold
product_sales = df.groupby('Item')['Units Sold'].sum().reset_index()

# Get top and bottom 10
top_10 = product_sales.sort_values(by='Units Sold', ascending=False).head(10)
bottom_10 = product_sales.sort_values(by='Units Sold', ascending=True).head(10)

# Add a label for color coding
top_10['Category'] = 'Top 10'
bottom_10['Category'] = 'Bottom 10'

# Combine and sort (ascending so items with less sales appear at the bottom)
combined = pd.concat([top_10, bottom_10]).sort_values(by='Units Sold')

# Color mapping
colors = combined['Category'].map({'Top 10': 'green', 'Bottom 10': 'red'})

# Plot horizontal bar chart
plt.figure(figsize=(10, 8))
bars = plt.barh(combined['Item'], combined['Units Sold'], color=colors, log=True)

# Add value labels to the right of the bars
for bar in bars:
    xval = bar.get_width()
    plt.text(xval + 0.2, bar.get_y() + bar.get_height()/2, f'{int(xval)}',
             va='center', fontsize=8)

# Aesthetics
plt.title('Top 10 & Bottom 10 Products Sold in November 2024 (Log Scale)', fontsize=14)
plt.xlabel('Units Sold (Log Scale)', fontsize=12)
plt.ylabel('Product', fontsize=12)
plt.tight_layout()
plt.grid(axis='x', linestyle='--', alpha=0.5)

plt.show()
