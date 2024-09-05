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




app = Flask(__name__)

WEBHOOK_VERIFY_TOKEN = "HAPPY"

@app.route("/whatsapp", methods=["GET"])

def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == WEBHOOK_VERIFY_TOKEN:
        print("Webhook verified successfully!")
        return challenge, 200
    else:
        return '', 403
    

@app.get("/")
def home():
    return "<p>Welcome to HTK API</p>"


@app.route("/whatsapp", methods=["POST"])


def handle_incoming_message():
    print("We outside!!!!")


if __name__ == "__main__":
    app.run()