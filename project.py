import pandas as pd
import matplotlib.pyplot as plt
file_path = 'task.csv'
df = pd.read_csv(file_path)
task_counts = df['Employe name'].value_counts()
plt.figure(figsize=(10, 6))
task_counts.plot(kind='bar', color='blue')
plt.title('Number of Tasks Completed by Each Employee(2000 to 2020)')
plt.xlabel('Employee Name')
plt.ylabel('Number of Tasks')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
