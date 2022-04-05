import csv
from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('Database.txt', mode='a')as database:
        email = data['email']
        name = data['name']
        message = data['message']
        file = database.write(f'\n{email},{name},{message}')


def write_to_csv(data):
    with open('Database.csv', newline='', mode='a')as database2:
        email = data['email']
        name = data['name']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('./thankyou.html')
    else:
        return 'something went wrong'





