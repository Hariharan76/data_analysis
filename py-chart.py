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

# Pie chart for hire counts
plt.figure(figsize=(12, 6))

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']

# Only include labels for months that have data
hire_labels = [months[i-1] for i in hire_counts.index]
relieve_labels = [months[i-1] for i in relieve_counts.index]

plt.subplot(1, 2, 1)
plt.pie(hire_counts, labels=hire_labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
plt.title('Hires Distribution for the Year ' + str(n))

# Pie chart for relieving counts
plt.subplot(1, 2, 2)
plt.pie(relieve_counts, labels=relieve_labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
plt.title('Relieving Distribution for the Year ' + str(n))

plt.tight_layout()

# Save the plot as an image
plt.savefig(f'monthly_hire_relieve_counts_pie.png')
plt.show()
