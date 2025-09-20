from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "centricia awesome"

#mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL-PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'jb831608@gmail.com'
app.config['MAIL_PASSWORD'] = 'xkxb jwlg lpjb lpkx'
app.config['MAIL_DEFAULT_SENDER'] = 'jb831608@gmail.com'

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

             msg = Message(f"New Contact Form Message {name}", recipients=["jb831608@gmail.com"])
             msg.body = f"""
             Name: {name}
             Email: {email}
             Message: {message}
             """
             mail.send(msg)
             flash("your message has been sent successfully", "success")
             return redirect(url_for('contact_us'))
        return render_template("contact us.html")

if __name__ =="__main__":
    app.run(host='0.0.0.0', debug=True)

