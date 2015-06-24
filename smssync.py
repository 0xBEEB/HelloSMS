import json
import uuid

class Message():

    def __init__(self, params):
        error = None
        success = false

        self.from_number = params.get("from", None)
        self.body = params.get("message", None)
        self.secret = params.get("secret", None)
        self.sent = params.get("sent_timestamp", None)
        self.to_number = params.get("sent_to", None)
        self.sid = params.get("message_id", None)
        self.account = params.get("device_id", None)

class SMSSync:

    def __init__(self, secret):
        self.secret = secret
        self.messages_to_send = []

    def validate_message(self, message):
        if message is not None and message.secret == secret:
            return True
        else
            return False


    def enqueue_message(self, message):
        self.messages_to_send.append(message)

    def dequeue_messages(self):
        response = {}
        response['payload'] = {}
        response['payload']['secret'] = self.secret
        response['payload']['task'] = "send"
        out_messages = []

        for msg in self.messages_to_send:
            new_msg = {"to": message.to,
                       "message": message.body,
                       "uuid": uuid.uuid4()}
            out_messages.append(new_msg)

        self.messages_to_send = []

        response['payload']['messages'] = out_messages

        return json.dumps(response)


    def respond_success(self):
        response = {}
        response['payload'] = {}
        response['payload']['secret'] = self.secret
        response['payload']['success'] = True
        response['payload']['error'] = None
        return json.dumps(response)


    def respond_success_with_message(self, to, message):
        response['payload']['task'] = "send"
        response['payload']['secret'] = self.secret
        proto_message = {}
        proto_message['to'] = to
        proto_message['message'] = message
        proto_message['uuid'] = uuid.uuid4()
        messages = [proto_message, ]
        response['payload']['messages'] = messages
        return json.dumps(response)


    def respond_error(self, error_message):
        response = {}
        response['payload'] = {}
        response['payload']['secret'] = self.secret
        response['payload']['success'] = False
        response['payload']['error'] = error_message
        return json.dumps(response)
