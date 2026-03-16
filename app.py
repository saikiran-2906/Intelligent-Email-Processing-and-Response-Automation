<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for, jsonify

from classifier import EmailClassifier
from responder import ResponseGenerator
from logger import EmailLogger

app = Flask(__name__)

classifier = EmailClassifier()
responder = ResponseGenerator()
logger = EmailLogger()

# Fake users for demo
users = {
    "customer1": {"password": "123", "role": "customer"},
    "admin1": {"password": "123", "role": "admin"},
    "support1": {"password": "123", "role": "support"}
}

@app.route("/")
def home():
    return render_template("login.html")


# LOGIN SYSTEM
@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    if username in users and users[username]["password"] == password:

        role = users[username]["role"]

        if role == "customer":
            return redirect("/customer")

        elif role == "admin":
            return redirect("/admin")

        elif role == "support":
            return redirect("/support")

    return "Invalid Login"


# CUSTOMER DASHBOARD
@app.route("/customer")
def customer():
    return render_template("customer.html")


# ADMIN DASHBOARD
@app.route("/admin")
def admin():
    return render_template("admin.html")


# SUPPORT DASHBOARD
@app.route("/support")
def support():
    return render_template("support.html")


# EMAIL PROCESSING
@app.route("/process", methods=["POST"])
def process_email():

    data = request.json

    subject = data["subject"]
    body = data["body"]

    text = subject + " " + body

    category = classifier.classify(text)

    reply = responder.generate(category)

    logger.log_email("customer", subject, category)

    return jsonify({
        "category": category,
        "reply": reply
    })


# VIEW LOGS (ADMIN)
@app.route("/logs")
def logs():
    return jsonify(logger.view_logs())


if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask, render_template, request, redirect, url_for, jsonify

from classifier import EmailClassifier
from responder import ResponseGenerator
from logger import EmailLogger

app = Flask(__name__)

classifier = EmailClassifier()
responder = ResponseGenerator()
logger = EmailLogger()

# Fake users for demo
users = {
    "customer1": {"password": "123", "role": "customer"},
    "admin1": {"password": "123", "role": "admin"},
    "support1": {"password": "123", "role": "support"}
}

@app.route("/")
def home():
    return render_template("login.html")


# LOGIN SYSTEM
@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    if username in users and users[username]["password"] == password:

        role = users[username]["role"]

        if role == "customer":
            return redirect("/customer")

        elif role == "admin":
            return redirect("/admin")

        elif role == "support":
            return redirect("/support")

    return "Invalid Login"


# CUSTOMER DASHBOARD
@app.route("/customer")
def customer():
    return render_template("customer.html")


# ADMIN DASHBOARD
@app.route("/admin")
def admin():
    return render_template("admin.html")


# SUPPORT DASHBOARD
@app.route("/support")
def support():
    return render_template("support.html")


# EMAIL PROCESSING
@app.route("/process", methods=["POST"])
def process_email():

    data = request.json

    subject = data["subject"]
    body = data["body"]

    text = subject + " " + body

    category = classifier.classify(text)

    reply = responder.generate(category)

    logger.log_email("customer", subject, category)

    return jsonify({
        "category": category,
        "reply": reply
    })


# VIEW LOGS (ADMIN)
@app.route("/logs")
def logs():
    return jsonify(logger.view_logs())


if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> d112ed5822a25c3f79603871755700285ffa1ed2
