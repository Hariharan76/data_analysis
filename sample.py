import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Haris@51",
    database="mydatabase"
)


mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM tbl_testing")
myresult = mycursor.fetchall()

column_names = [i[0] for i in mycursor.description]


df = pd.DataFrame(myresult, columns=column_names)


mycursor.close()
mydb.close()



sampling_condition_counts = df['sampling_condition'].value_counts()
print(sampling_condition_counts)


plt.figure(figsize=(10, 6))
sns.barplot(x=sampling_condition_counts.index, y=sampling_condition_counts.values, palette='viridis')
plt.title('Sampling Condition Counts')
plt.xlabel('Sampling Condition')
plt.ylabel('Count')
plt.xticks(rotation=45)  
plt.show()
