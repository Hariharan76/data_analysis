import mysql.connector
from fpdf import FPDF
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Haris@51",
    database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM tbl_form_detail")
myresult = mycursor.fetchall()
column_names = [i[0] for i in mycursor.description]
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        for column_title in column_names:
            self.cell(40, 10, column_title, border=1)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

pdf = PDF()
pdf.add_page()

pdf.set_font('Arial', 'B', 12)
for column_title in column_names:
    pdf.cell(40, 10, column_title, border=1)
pdf.ln(10)


pdf.set_font('Arial', '', 12)
for row_data in myresult:
    for cell_value in row_data:
        pdf.cell(40, 10, str(cell_value), border=1)
    pdf.ln(10)

pdf.output('FormDetails.pdf')

print("Data has been written to FormDetails.pdf")
