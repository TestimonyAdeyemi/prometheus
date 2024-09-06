import os
import requests
import flask
from flask import Flask, request
import logging


url = "https://graph.facebook.com/v20.0/396015606935687/messages"

# #print(os.getenv('WHATSAPP_API_TOKEN'))

# Define the headers
headers = {
    "Authorization": "Bearer EAAPPDu1MMoEBOxILlczGwD9VXUSXeVqadzvCBDbZBagpZASSjty90cgWL6VFnprRifXDviIScMF3xKAJNccTiowh7Kzfz7YaecoVs43TxPSMYfFTcPkmI9w2fdLpYZB0q7mkvuRcjdYcHLYDxfwdiR1MPI1oEvxg8wHfTBiDeO9VcMdOvYZCcA5CiapB3bHnFqAeZAZAC0meO05o0STrSBUPlMrziJ8CIlOPsZD",
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


# @app.route("/", methods=["GET"])
# def root():
#     if "hub.mode" in request.args:
#         return verify_webhook()
#     return "<p>Welcome to HTK API</p>"


@app.route("/whatsapp", methods=["GET"])
def whatsapp_verify():
    # Assuming verify_webhook handles verification challenge from WhatsApp
    return verify_webhook()

@app.route("/whatsapp", methods=["POST"])
def handle_incoming_message():
    try:

        # Attempt to parse the incoming JSON request
        message = request.get_json(silent=True)
        print(message)
        
        return "OK", 200

    except Exception as e:
        # Log any exception that occurs for debugging purposes
        app.logger.error(f"Error processing incoming message: {str(e)}")
        return "Internal Server Error", 500



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




