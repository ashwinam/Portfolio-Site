import csv
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/works')
def projects():
    return render_template('projects.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


def write_to_file(data):
    with open('./database.txt', mode='a') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        db.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('./database.csv', newline='', mode='a') as db2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(
            db2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return render_template('thankyou.html')
    else:
        return 'Something went wrong, Try Again!'
