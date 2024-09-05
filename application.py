import os
import requests
import flask
from flask import Flask, request


# url = "https://graph.facebook.com/v19.0/228794113648969/messages"

# #print(os.getenv('WHATSAPP_API_TOKEN'))

# # Define the headers
# headers = {
#     "Authorization": "Bearer EAAQyAvDp7hIBO1qJ1PCXPGwGZBtQl593EmoEIQJQVhgzivwYWTGVvCoQs7SDDtx6DZBWNvhH9LiuVRDXstBXJiBAawGaZAN9FSWtZBkL3eQqu8oQZAYKSL03WGEDRhQLAxBBSZCy3MpZAjrg95YSPNJ8a5Nm5QgJZCIfiuqn1ZByM3geoB81T9FfuZChJAEobv5E0BZBAmYUa9902OfW9gACv9bLT1uqAKwbTjFg44Y",
#     "Content-Type": "application/json"
# }



import os
from flask import Flask, request

port = int(os.environ.get('PORT', 4000))

app = Flask(__name__)

WEBHOOK_VERIFY_TOKEN = "HAPPY"

@app.route("/whatsapp", methods=["GET"])
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

@app.route("/")
def home():
    return "<p>Welcome to HTK API</p>"

@app.route("/whatsapp", methods=["POST"])
def handle_incoming_message():
    print("Received incoming message")
    # Here you would typically process the incoming message
    # For now, we'll just print the raw data
    print(request.get_json())
    return "OK", 200

if __name__ == "__main__":
    print(f"Starting server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=True)