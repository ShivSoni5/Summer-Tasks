from flask import Flask, request, render_template
import mysql.connector as mysql

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        age = int(request.form['age'])
#        print(first_name, last_name, age)
        mariadb = mysql.connect(user='raj',password='redhat',database='PandaProject')
        cursor = mariadb.cursor()
        query = (f'insert into userdata(First_Name, Second_Name, Age) values("{first_name}","{last_name}",{age});')
        cursor.execute(query)
        mariadb.commit()
        mariadb.close()

    return render_template('get_data.html')


if __name__ == '__main__':
    app.run(debug=True)
