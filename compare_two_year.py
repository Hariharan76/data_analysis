import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('employees.csv')
df['HIRE_DATE'] = pd.to_datetime(df['HIRE_DATE'])
df['RELIEVING_DATE'] = pd.to_datetime(df['RELIEVING_DATE'])
df['HIRE_YEAR'] = df['HIRE_DATE'].dt.year
df['HIRE_MONTH'] = df['HIRE_DATE'].dt.month
df['RELIEVE_YEAR'] = df['RELIEVING_DATE'].dt.year
df['RELIEVE_MONTH'] = df['RELIEVING_DATE'].dt.month
year1 = int(input("Enter the first year: "))
year2 = int(input("Enter the second year: "))
df_year1 = df[df['HIRE_YEAR'] == year1]
df_year2 = df[df['HIRE_YEAR'] == year2]
hire_counts_year1 = df_year1['HIRE_MONTH'].value_counts().sort_index()
relieve_counts_year1 = df_year1['RELIEVE_MONTH'].value_counts().sort_index()
hire_counts_year2 = df_year2['HIRE_MONTH'].value_counts().sort_index()
relieve_counts_year2 = df_year2['RELIEVE_MONTH'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
bar_width = 0.35
bar_positions_hire_year1 = np.arange(len(hire_counts_year1))
bar_positions_relieve_year1 = np.arange(len(relieve_counts_year1)) + bar_width
bar_positions_hire_year2 = np.arange(len(hire_counts_year2)) + 2 * bar_width
bar_positions_relieve_year2 = np.arange(len(relieve_counts_year2)) + 3 * bar_width
plt.bar(bar_positions_hire_year1, hire_counts_year1.values, width=bar_width, color='blue', label=f'Hires {year1}')
plt.bar(bar_positions_relieve_year1, relieve_counts_year1.values, width=bar_width, color='red', label=f'Relieving {year1}')
plt.bar(bar_positions_hire_year2, hire_counts_year2.values, width=bar_width, color='green', label=f'Hires {year2}')
plt.bar(bar_positions_relieve_year2, relieve_counts_year2.values, width=bar_width, color='yellow', label=f'Relieving {year2}')
plt.xlabel('Month')
plt.ylabel('Number of Employees')
plt.title(f'Monthly Hire and Relieving Counts for Years {year1} and {year2}')
plt.xticks(ticks=np.arange(12) + bar_width, labels=[
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 
    'August', 'September', 'October', 'November', 'December'], rotation=45)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
# Save the plot as an image
plt.savefig(f'monthly_hire_relieve_counts_{year1}_{year2}.png')
plt.show()
