import pandas as pd
import matplotlib.pyplot as plt

# Load data
file_path = 'monthly_combined.xlsx'  # change to your file path
df = pd.read_excel(file_path)

# Convert date if needed
df['Date'] = pd.to_datetime(df['Date'])

# Aggregate total units sold by product
total_units = df.groupby('Item')['Units Sold'].sum()

# Get top 20 products by units sold
top_20 = total_units.sort_values(ascending=False).head(20)

# Calculate cumulative percentage
cum_perc = top_20.cumsum() / top_20.sum() * 100

# Plotting
fig, ax1 = plt.subplots(figsize=(12, 6))

# Bar plot for units sold
ax1.bar(top_20.index, top_20.values, color='skyblue')
ax1.set_ylabel('Units Sold', color='blue')
ax1.set_xticklabels(top_20.index, rotation=45, ha='right')
ax1.tick_params(axis='y', labelcolor='blue')

# Line plot for cumulative percentage
ax2 = ax1.twinx()
ax2.plot(top_20.index, cum_perc, color='red', marker='D', ms=7)
ax2.set_ylabel('Cumulative Percentage (%)', color='red')
ax2.tick_params(axis='y', labelcolor='red')
ax2.axhline(80, color='gray', linestyle='--', linewidth=1)  # 80% line

plt.title('Pareto Chart: Top 20 Products by Units Sold')
plt.tight_layout()
plt.show()
