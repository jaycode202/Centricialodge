from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')

mail = Mail(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about us")
def about_us():
    return render_template("about us.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact us", methods=["GET", "POST"])
def contact_us():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(
            subject=f"New Contact Form Message from {name}",
            recipients=[os.environ.get('MAIL_USERNAME')],
            body=f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
        )

        try:
            mail.send(msg)
            flash("Your message has been sent successfully!", "success")
        except Exception as e:
            flash(f"Error sending message: {e}", "danger")
            print("Mail send error:", e)  # <-- This will show in Render logs

        return redirect(url_for('contact_us'))

    return render_template("contact us.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)






