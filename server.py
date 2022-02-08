from flask_mail import Mail
from flask import Flask, render_template, request
import csv
import sqlite3

app = Flask(__name__)

# Configuration for flask-mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


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


# def write_to_file(data):
#     with open('./database.txt', mode='a') as db:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         db.write(f'\n{email}, {subject}, {message}')


# def write_to_csv(data):
#     with open('./database.csv', newline='', mode='a') as db2:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         csv_writer = csv.writer(
#             db2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         csv_writer.writerow([email, subject, message])


# def write_to_db(data):
#     email = data['email']
#     subject = data['subject']
#     message = data['message']
#     connection = sqlite3.connect(
#         "contacts.db", check_same_thread=False)  # initialize DB
#     cursor = connection.cursor()
#     cursor.execute(
#         "CREATE TABLE IF NOT EXISTS contacts (Email text, Subject text, Message text)")
#     cursor.execute("INSERT INTO contacts VALUES(?,?,?)",
#                    [email, subject, message])

#     for rows in cursor.execute("SELECT * FROM contacts"):
#         print(rows)
#     connection.close()


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            email = data['email']
            subject = data['subject']
            message = data['message']
            mail.send_message('Message from ' + email + ' and subject is ' + subject,
                              sender=data['email'], recipients=[app.config['MAIL_USERNAME']], body=f' you will receive message from {email} this and the message is  {message}')
            return render_template('thankyou.html')
        except:
            print('Something Wrong')
    else:
        return 'Something went wrong, Try Again!'


if __name__ == '__main__':
    app.run(debug=True, port=3500)
