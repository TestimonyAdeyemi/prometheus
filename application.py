import os
import requests
import flask
from flask import Flask, request
import logging


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



# @app.route("/", methods=["GET"])
# def root():
#     if "hub.mode" in request.args:
#         return verify_webhook()
#     return "<p>Welcome to HTK API</p>"




# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route("/whatsapp", methods=["GET"])
def whatsapp_verify():
    # Assuming verify_webhook handles verification challenge from WhatsApp
    return verify_webhook()

@app.route("/whatsapp", methods=["POST"])
def handle_incoming_message():
    try:
        # Log that a message was received
        app.logger.debug("Received POST request on /whatsapp")

        # Check headers to ensure content type is application/json
        if request.content_type != 'application/json':
            app.logger.warning(f"Unexpected content type: {request.content_type}")
            return "Unsupported Media Type", 415

        # Log raw incoming data
        raw_data = request.data
        app.logger.debug(f"Raw data received: {raw_data}")

        # Attempt to parse the incoming JSON request
        message = request.get_json(silent=True)

        # Log if JSON parsing fails
        if message is None:
            app.logger.error("Failed to parse JSON from the incoming request")
            return "Bad Request", 400

        # Log the parsed JSON message
        app.logger.debug(f"Parsed JSON message: {message}")

        # If specific structure is expected, log its presence or absence
        if 'entry' in message:
            app.logger.info(f"Received entry: {message['entry']}")
        else:
            app.logger.warning(f"Unexpected message format: {message}")

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




