import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
file_path = 'monthly_sales.xlsx'
df = pd.read_excel(file_path)

df['Date'] = pd.to_datetime(df['Date'])

# Extract brand (using same function as before)
brands = [
    'APSARA', 'CASIO', 'Cello', 'Classmate', 'DOMS', 'FLAIR',
    'HAUSER', 'LUXOR', 'NAVNEET', 'PARKER', 'PIERRE CARDIN',
    'Pilot', 'Reynolds'
]

def extract_brand(item):
    words = str(item).split()
    first_word = words[0] if len(words) > 0 else ''
    first_two = ' '.join(words[:2]) if len(words) > 1 else first_word
    brands_upper = [b.upper() for b in brands]
    if first_word.upper() in brands_upper:
        return first_word
    elif first_two.upper() in brands_upper:
        return first_two
    else:
        return 'Other'

df['Brand'] = df['Item'].apply(extract_brand)
df_brand = df[df['Brand'] != 'Other']

# Total units sold per brand (all months combined)
total_sales = df_brand.groupby('Brand')['Units Sold'].sum()

# Sort descending
total_sales = total_sales.sort_values(ascending=False)

# Plot bar chart
plt.figure(figsize=(12, 6))
sns.barplot(x=total_sales.values, y=total_sales.index, palette="viridis")

plt.title('Total Units Sold per Brand (Descending Order)', fontsize=16)
plt.xlabel('Units Sold')
plt.ylabel('Brand')
plt.tight_layout()
plt.show()
