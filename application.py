import os
import requests
import flask
from flask import Flask, request


url = "https://graph.facebook.com/v19.0/228794113648969/1180888120028690/messages"

# #print(os.getenv('WHATSAPP_API_TOKEN'))

# Define the headers
headers = {
    "Authorization": "Bearer EAAQyAvDp7hIBO4eE2XhzfI4PAZCdvXrnJEVBCZAMRP9q4ZBPTYEcsmK7vcZCv06XY8N8lntW8EV8C0ZClk4o5myXpoqcHdeAtLR4fVLHH6oeDTZCSuSKGZCbPBwROs9xYTpcLrWsbyqzStCQeZCZBip4L2QwZBohWvwyZBuGDvhVcUN5LDZBNrXJkdWFZBnJNEM3j4KomssjbEZB622bAMswxHdOFOCit3ZC7bsefWqdBgZD",
    "Content-Type": "application/json"
}


import os
from flask import Flask, request

port = int(os.environ.get('PORT', 4000))

app = Flask(__name__)

WEBHOOK_VERIFY_TOKEN = "HAPPY"

def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    print(f"Verification attempt - Mode: {mode}, Token: {token}, Challenge: {challenge}")

    if mode == "subscribe" and token == WEBHOOK_VERIFY_TOKEN:
        print("Webhook verified successfully!")
        return str(challenge), 200
    else:
        print("Webhook verification failed.")
        return '', 403

@app.route("/", methods=["GET"])
def root():
    if "hub.mode" in request.args:
        return verify_webhook()
    return "<p>Welcome to HTK API</p>"

@app.route("/whatsapp", methods=["GET"])
def whatsapp_verify():
    return verify_webhook()


@app.route("/whatsapp", methods=["POST"])
def handle_incoming_message():
    print("I got a message")
    message = request.json
    print(message)
    
    print(request.get_json())
    return "OK", 200

if __name__ == "__main__":
    print(f"Starting server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=True)











# app_id = "6979647548799998"

#     if data['entry'][0]['changes'][0]['value']['metadata']['phone_number_id'] != os.getenv(f"PHONE_NUMBER_ID_{app_id}"):
#         return "Incorrect app", 403
#     # Process the message...
#     print("Received incoming message")


#     data = {
#             "messaging_product": "whatsapp",
#             "to": "2348143237903",
#             "type": "text",
#             "text": {
#                 "body": "friend, don't reply"
#             }
#         }

#     response = requests.post(url, headers=headers, json=data)




