import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

n = int(input("Enter the year:"))

df = pd.read_csv('employees.csv')
df['HIRE_DATE'] = pd.to_datetime(df['HIRE_DATE'])

df['HIRE_YEAR'] = df['HIRE_DATE'].dt.year
df['HIRE_MONTH'] = df['HIRE_DATE'].dt.month

df['RELIEVING_DATE'] = pd.to_datetime(df['RELIEVING_DATE'])

df_year = df[df['HIRE_YEAR'] == n]

hire_counts = df_year['HIRE_MONTH'].value_counts().sort_index()
relieve_counts = df_year['RELIEVING_DATE'].dt.month.value_counts().sort_index()
plt.figure(figsize=(10, 6))
bar_positions_hire = np.arange(len(hire_counts))
bar_positions_relieve = np.arange(len(relieve_counts)) + 0.4
plt.bar(bar_positions_hire, hire_counts.values, width=0.4, color='blue', label='Hires')
plt.bar(bar_positions_relieve, relieve_counts.values, width=0.4, color='red', label='Relieving')
plt.xlabel('Month')
plt.ylabel('Number of Employees')
plt.title(f'Monthly Hire and Relieving Counts for the Year {n}')
plt.xticks(ticks=np.arange(12), labels=[
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 
    'August', 'September', 'October', 'November', 'December'], rotation=45)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the plot as an image
plt.savefig(f'monthly_hire_relieve_counts.png')
plt.show()
