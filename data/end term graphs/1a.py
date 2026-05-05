import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Excel file
df = pd.read_excel('monthly_sales.xlsx')

# Step 2: Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Step 3: Group by Date and sum the Revenue
daily_revenue = df.groupby('Date')['Revenue'].sum().reset_index()

# Step 4: Plot the daily revenue
plt.figure(figsize=(10, 5))
plt.plot(daily_revenue['Date'], daily_revenue['Revenue'], marker='o')
plt.xlabel('Date')
plt.ylabel('Daily Revenue (₹)')
plt.title('Daily Revenue Trends for November 2024')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
