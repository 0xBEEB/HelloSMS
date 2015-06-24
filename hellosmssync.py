from flask import Flask, request, redirect
from smssync import SMSSync, Message

app = Flask(__name__)
SUPERSECRET = "SpArCkLeP0Nies!"

@app.route("/", methods=['GET', 'POST'])
def hello_sms():
    """Respond to incoming sms with a simple message."""
    message = Message(request.values)
    smssyncClient = SMSSync(SUPERSECRET)
    response = ""
    if not smssyncClient.validate_message(message):
        response = smssyncClient.respond_error("Incorrect secret")
    if message.to is not None and len(messages.to) > 0:
        response = smssyncClient.respond_success_with_message(message.to, "Hello, World!")
    else:
        response = smsClient.respond_error("Could not read incoming number")
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
