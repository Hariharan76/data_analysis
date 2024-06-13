import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('employees.csv')
df['HIRE_DATE'] = pd.to_datetime(df['HIRE_DATE'])
df['RELIEVING_DATE'] = pd.to_datetime(df['RELIEVING_DATE'])

year1 = int(input("Enter the first year: "))
year2 = int(input("Enter the second year: "))

# Filter data by year
df_year1 = df[df['HIRE_DATE'].dt.year == year1]
df_year2 = df[df['HIRE_DATE'].dt.year == year2]

# Group data by month and count
hire_counts_year1 = df_year1['HIRE_DATE'].dt.month.value_counts().sort_index().fillna(0)
relieve_counts_year1 = df_year1['RELIEVING_DATE'].dt.month.value_counts().sort_index().fillna(0)
hire_counts_year2 = df_year2['HIRE_DATE'].dt.month.value_counts().sort_index().fillna(0)
relieve_counts_year2 = df_year2['RELIEVING_DATE'].dt.month.value_counts().sort_index().fillna(0)

# Create DataFrames for plotting
data_year1_hires = {
    'Month': hire_counts_year1.index,
    'Hires': hire_counts_year1.values,
    'Year': year1
}
data_year1_relieving = {
    'Month': relieve_counts_year1.index,
    'Relieving': relieve_counts_year1.values,
    'Year': year1
}
data_year2_hires = {
    'Month': hire_counts_year2.index,
    'Hires': hire_counts_year2.values,
    'Year': year2
}
data_year2_relieving = {
    'Month': relieve_counts_year2.index,
    'Relieving': relieve_counts_year2.values,
    'Year': year2
}
df_year1_hires = pd.DataFrame(data_year1_hires)
df_year1_relieving = pd.DataFrame(data_year1_relieving)
df_year2_hires = pd.DataFrame(data_year2_hires)
df_year2_relieving = pd.DataFrame(data_year2_relieving)

# Plot using Seaborn
plt.figure(figsize=(12, 6))

# Plot for year 1 hiring counts
plt.subplot(2, 2, 1)
sns.barplot(data=df_year1_hires, x='Month', y='Hires', palette='viridis', alpha=0.8)
plt.xlabel('Month')
plt.ylabel('Number of Employees')
plt.title(f'Hiring Counts for Year {year1}')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Plot for year 1 relieving counts
plt.subplot(2, 2, 2)
sns.barplot(data=df_year1_relieving, x='Month', y='Relieving', palette='viridis', alpha=0.8)
plt.xlabel('Month')
plt.ylabel('Number of Employees')
plt.title(f'Relieving Counts for Year {year1}')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Plot for year 2 hiring counts
plt.subplot(2, 2, 3)
sns.barplot(data=df_year2_hires, x='Month', y='Hires', palette='viridis', alpha=0.8)
plt.xlabel('Month')
plt.ylabel('Number of Employees')
plt.title(f'Hiring Counts for Year {year2}')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Plot for year 2 relieving counts
plt.subplot(2, 2, 4)
sns.barplot(data=df_year2_relieving, x='Month', y='Relieving', palette='viridis', alpha=0.8)
plt.xlabel('Month')
plt.ylabel('Number of Employees')
plt.title(f'Relieving Counts for Year {year2}')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
