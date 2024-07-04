from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)

app.secret_key = '2005'

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.mail.yahoo.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'thompsonrejen@yahoo.com'
app.config['MAIL_PASSWORD'] = 'Thamaraitnj'

mail = Mail(app)

@app.route('/about')
def about():
    return render_template('templates/thomp.html')  # Update with your about page template

@app.route('/projects')
def projects():
    return render_template('templates/projects.html')

@app.route('/contact')
def contact():
    return render_template('templates/contactc.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(subject='New message from your portfolio website',
                      sender=email,
                      recipients=['your_email@gmail.com'])
        msg.body = f'You have received a new message from {name} ({email}):\n\n{message}'
        mail.send(msg)

        return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(debug=True)
