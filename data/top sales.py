import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# === Configuration ===
file_path = r"monthly_combined.xlsx"
item_col = 'Item'
quantity_col = 'Units Sold'

# === Load the Data ===
try:
    df = pd.read_excel(file_path)
except Exception as e:
    print(f"Error loading file: {e}")
    exit()

# === Validate Columns ===
if item_col not in df.columns or quantity_col not in df.columns:
    print(f"Missing required columns. Found columns: {list(df.columns)}")
    exit()

# === Clean and Process ===
df[quantity_col] = pd.to_numeric(df[quantity_col], errors='coerce').fillna(0)
sales_summary = df.groupby(item_col)[quantity_col].sum().sort_values()

# === Get Bottom & Top 10 ===
bottom_10 = sales_summary.head(10)
top_10 = sales_summary.tail(10)

# === Combine & Create Color List ===
combined = pd.concat([bottom_10, top_10])
colors = ['red'] * len(bottom_10) + ['green'] * len(top_10)

# === Plotting ===
plt.figure(figsize=(14, 8))
bars = plt.barh(combined.index, combined.values, color=colors)
plt.xscale('log')
plt.xlabel('Units Sold (Log Scale)', fontsize=12)
plt.title('Top 10 & Bottom 10 Products Sold in a Month (Log Scale)', fontsize=14, fontweight='bold')

# Add Value Labels
for bar in bars:
    width = bar.get_width()
    color = 'darkred' if bar.get_facecolor()[0] > 0.8 else 'darkgreen'
    plt.text(width * 1.05, bar.get_y() + bar.get_height()/2,
             f'{int(width)}', va='center', ha='left', fontsize=10, color=color)

plt.tight_layout()
plt.grid(True, which="both", axis="x", linestyle='--', linewidth=0.5, alpha=0.7)

# === Legend ===
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='green', label='Top 10 Products'),
                   Patch(facecolor='red', label='Bottom 10 Products')]
plt.legend(handles=legend_elements, loc='lower right')

plt.show()
