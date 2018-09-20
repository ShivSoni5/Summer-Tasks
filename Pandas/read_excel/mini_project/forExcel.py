from flask import Flask, request, render_template
import pandas as pd
import os
import xlsxwriter

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        age = request.form['age']

        if os.path.exists('pandas.xlsx') is False:
            create_file()
            insert_data(first_name, last_name, age)

        else:
            insert_data(first_name, last_name, age)


    return render_template('get_data.html')

def create_file():
    workbook = xlsxwriter.Workbook('pandas.xlsx')
    worksheet = workbook.add_worksheet()
    workbook.close()

def insert_data(FirstName, LastName, Age):
    out = pd.read_excel('pandas.xlsx')
    df = pd.DataFrame({'First Name': [FirstName], 'Last Name': [LastName], 'Age': [Age]})
    append_data = pd.concat([out,df]) 

    writer = pd.ExcelWriter('pandas.xlsx', engine='xlsxwriter')
    append_data.to_excel(writer, sheet_name='Sheet1', index=0)
    writer.save()

if __name__ == '__main__':
    app.run(debug=True)
