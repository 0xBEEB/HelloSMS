from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_sms():
    """Respond to incoming sms with a simple message."""

    resp = twilio.twiml.Response()
    resp.message("Hello, World!")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
