from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        print(first_name, last_name)
    return render_template('get_data.html')


if __name__ == '__main__':
    app.run()
