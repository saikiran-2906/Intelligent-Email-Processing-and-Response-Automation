from flask import Flask,render_template,request,jsonify
from classifier import EmailClassifier
from responder import ResponseGenerator
from logger import EmailLogger

app=Flask(__name__)

classifier=EmailClassifier()
responder=ResponseGenerator()
logger=EmailLogger()

@app.route("/")
def home():

    return render_template("index.html")


@app.route("/process",methods=["POST"])

def process_email():

    data=request.json

    sender=data["sender"]
    subject=data["subject"]
    body=data["body"]

    text=subject+" "+body

    category=classifier.classify(text)

    reply=responder.generate(category)

    logger.log_email(sender,subject,category)

    return jsonify({

    "category":category,
    "reply":reply

    })


if __name__=="__main__":

    app.run(debug=True)