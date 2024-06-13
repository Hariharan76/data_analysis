import mysql.connector
import pandas as pd
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Haris@51",
    database="mydatabase"
)
mycursor = mydb.cursor()
columns1 = int(input("how many coloumn you wanted: "))
columns =[] 
for i in range(columns1):
    n=input("Enter the coloumn name: ")
    columns.append(n)
if len(columns)>1:
    columns_str = ", ".join(columns)
else:
    columns_str = columns[0]
query = f"SELECT {columns_str} FROM tbl_format_category"
mycursor.execute(query)
myresult = mycursor.fetchall()
df = pd.DataFrame(myresult, columns=columns)


df.to_excel("output1.xlsx", index=False)

print("Data has been successfully written to output.xlsx")
