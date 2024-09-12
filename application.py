import os
import requests
import flask
from flask import Flask, request
import logging
from flask import Flask, request, jsonify

import json
import google.generativeai as genai






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





app = Flask(__name__)

# Define allowed display phone number and phone number ID
ALLOWED_DISPLAY_PHONE_NUMBER = "2347070471117"
ALLOWED_PHONE_NUMBER_ID = "396015606935687"

@app.before_request
def validate_request():
    # Only run validation for POST requests to the /whatsapp endpoint
    if request.method == "POST" and request.path == "/whatsapp":
        try:
            # Extract JSON payload from incoming request
            data = request.get_json()
            if not data:
                print("No JSON payload received.")
                return jsonify({"error": "Bad Request"}), 400

            # Navigate through payload to extract phone number details
            entry = data.get('entry', [])
            if not entry:
                print("No entry in the payload.")
                return jsonify({"error": "Bad Request"}), 400
            
            changes = entry[0].get('changes', [])
            if not changes:
                print("No changes in the entry.")
                return jsonify({"error": "Bad Request"}), 400

            value = changes[0].get('value', {})
            metadata = value.get('metadata', {})
            display_phone_number = metadata.get('display_phone_number')
            phone_number_id = metadata.get('phone_number_id')

            # Validate the incoming display phone number and phone number ID
            if (display_phone_number != ALLOWED_DISPLAY_PHONE_NUMBER or 
                phone_number_id != ALLOWED_PHONE_NUMBER_ID):
                print(f"Rejected request from display number: {display_phone_number}, phone ID: {phone_number_id}")
                return jsonify({"error": "Forbidden"}), 403  # Reject the request early
            
        except Exception as e:
            print(f"Error during request validation: {e}")
            return jsonify({"error": "Internal Server Error"}), 500


MY_BUSINESS_PHONE_NUMBER = "2347070471117"

@app.route("/whatsapp", methods=["POST"])

def handle_incoming_message():
    # If the request passes validation, process it here
    message = request.get_json()
    print("Processing message:", message)

    # Extract 'body' from the message
    body = message['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']

    # Extract 'wa_id' from the contact
    wa_id = message['entry'][0]['changes'][0]['value']['contacts'][0]['wa_id']

    # File path for user history
    history_file = f"user_{wa_id}_history.json"

    # Check if user history exists
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            chat_history = json.load(f)
    else:
        chat_history = []

    # Configure Gemini AI
    genai.configure(api_key=os.environ["AIzaSyDmX5Z5gwQ2v_Y696AjLRZgM0LyHNo91o4"])

    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        system_instruction="You are the customer representative for this business\n\n[Your system instruction here...]"
    )

    # Start chat session with existing history
    chat_session = model.start_chat(history=chat_history)

    # Send user message and get response
    response = chat_session.send_message(body)

    # Update chat history
    chat_history.append({"role": "user", "parts": [body]})
    chat_history.append({"role": "model", "parts": [response.text]})

    # Save updated chat history
    with open(history_file, 'w') as f:
        json.dump(chat_history, f)

    # Send response back to WhatsApp
    url = "https://graph.facebook.com/v20.0/396015606935687/messages"
    headers = {
        "Authorization": "Bearer EAAPPDu1MMoEBO4p1DoaeusIUfX4hAzXcKelPMEdJeeTjI46KvJcZBJYhvNZAmJxCjCJ89gMuQlmUPXxPN9atBx7viux3Dskk1mA44MW3P1H7mdz078CuHxQzOh98d5ozblkvxWDlHafIZCkZBGr3vemJVs7hZAePO3ZCl4aax5CJddUnF6jELmCZBwgn3LZCQaeVrZCT4GxBZAMkUbOkaTnDtS1644Dfy6D1MzUF9EdZBw180gZD",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": wa_id,
        "type": "text",
        "text": {
            "body": response.text
        }
    }

    response = requests.post(url, headers=headers, json=data)

    return "OK", 200

if __name__ == "__main__":
    print(f"Starting server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=True)










