from flask import Flask, request, render_template
import pandas as pd

data = pd.DataFrame(columns=['First Name','Second Name','Age'])
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        age = int(request.form['age'])
        writer = pd.ExcelWriter('first.xlsx', engine='xlsxwriter')
        global data
        data1 = pd.DataFrame([first_name],columns=['First Name'])
        data2 = pd.DataFrame([last_name],columns=['Second Name'])
        data3 = pd.DataFrame([age],columns=['Age'])
        data = data.append([[data1],[data2],[data3]])
#        data = data.append(data1)
#        data = data.append(data2)
#        data = data.append(data3)
        data.to_excel(writer, sheet_name = 'Sheet1')
        writer.save()

    return render_template('get_data.html')


if __name__ == '__main__':
    app.run(debug=True)
