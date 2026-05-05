import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your Excel file
file_path = 'monthly_combined.xlsx'  # Update this path
df = pd.read_excel(file_path)

# Check your columns; assuming: 'Date', 'Item', 'Units Sold', 'Revenue' exist

# Convert 'Date' to datetime if not already
df['Date'] = pd.to_datetime(df['Date'])

# Aggregate by month (change to day if you want daily heatmap)
df['Month'] = df['Date'].dt.to_period('M').astype(str)

# Aggregate total units sold by product
total_units = df.groupby('Item')['Units Sold'].sum()

# Get top 20 products
top_products = total_units.sort_values(ascending=False).head(20).index.tolist()

# Filter data for only top products
df_top = df[df['Item'].isin(top_products)]

# Create pivot table: rows = products, columns = months, values = sum of units sold
pivot = df_top.pivot_table(
    index='Item',
    columns='Month',
    values='Units Sold',
    aggfunc='sum',
    fill_value=0
)

# Sort products by total units sold descending
pivot = pivot.loc[top_products]

# Plotting heatmap
plt.figure(figsize=(14, 10))
sns.heatmap(pivot, annot=True, fmt='g', cmap='coolwarm', linewidths=0.5, linecolor='gray')

plt.title('Heatmap of Top 20 Products Sold by Month')
plt.ylabel('Product')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()
