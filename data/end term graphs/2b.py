import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load your sales data
df = pd.read_excel("monthly_sales.xlsx")

# Step 2: Ensure 'Date' is datetime type and remove time
df['Date'] = pd.to_datetime(df['Date']).dt.date

# Step 3: Identify top 20 products by total units sold
top_products = df.groupby('Item')['Units Sold'].sum().sort_values(ascending=False).head(20).index

# Step 4: Filter data for those products only
df_top = df[df['Item'].isin(top_products)]

# Step 5: Create pivot table: rows = products, columns = dates, values = units sold
sales_frequency = df_top.pivot_table(
    index='Item',
    columns='Date',
    values='Units Sold',
    aggfunc='sum',
    fill_value=0
)

# Step 6: Plot heatmap with centered tick labels
plt.figure(figsize=(14, 8))
ax = sns.heatmap(sales_frequency, cmap='YlGnBu', linewidths=0.5, linecolor='gray')

# Fix: Center-align x-axis date labels
ax.set_xticks([x + 0.5 for x in range(len(sales_frequency.columns))])  # Offset to center
ax.set_xticklabels(sales_frequency.columns, rotation=45, ha='right')   # Keep 45° rotation

plt.title('Heatmap of Daily Sales for Top 20 Products')
plt.xlabel('Date')
plt.ylabel('Product')
plt.tight_layout()
plt.show()
