import mysql.connector
import pandas as pd
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Haris@51",
    database="mydatabase"
)
mycursor = mydb.cursor()
query = "SELECT * FROM tbl_format_category"
mycursor.execute(query)
myresult = mycursor.fetchall()
column_names = [i[0] for i in mycursor.description]
df = pd.DataFrame(myresult, columns=column_names)
json_result = df.to_json(orient="records")
print(json_result)
