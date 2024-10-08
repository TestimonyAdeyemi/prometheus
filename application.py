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
    print(message)
    print("Processing message:", message)

    # Extract 'body' from the message
    body = message['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']

    try:
        body = message['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
        print(f"Message body: {body}")



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




        
        from groq import Groq

        # Add your API key here
        api_key = "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"

        # Instantiate the client with the API key
        client = Groq(api_key=api_key)

        # Store the output in a variable
        output = ""

        completion = client.chat.completions.create(
            model="llama-3.2-11b-text-preview",
            messages=[
                {
                    "role": "system",
                    "content": "what is the mood of this message, 1. sad, 2. angry 3.happy 4. Neutral.\nReply me only with a number between 1 and 4. Do not give any explanations."
                },
                {
                    "role": "user",
                    "content": body
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )

        # Append the output to the variable
        for chunk in completion:
            output += chunk.choices[0].delta.content or ""

        # Now `output` holds the response from the model
        print(f"user mood of {output}")




        # Update chat history
        chat_history.append({"role": "user", "parts": [body]})
        chat_history.append({"role": "model", "parts": [output]})

        # Save updated chat history
        with open(history_file, 'w') as f:
            json.dump(chat_history, f)

        # Send response back to WhatsApp
        url = "https://graph.facebook.com/v20.0/396015606935687/messages"
        headers = {
            "Authorization": "Bearer EAAPPDu1MMoEBOy8xa6fZAG8p7JJiDa3ZCX6pVT0qCKkZCENnCZAmdpLcVtbkeLOhINaRcV4NUvNHd3RZAdKnBFTNbgQ9CwaQP5rZBLeCpVeLIA6fv0AvoshJdm8IwTBiKbVBljKwXKVD3jZCmEdOfC9Gg5RumUJu41iQU3GaDZCxfUsZAsLYaVeyle25YWEOBwUsc5eT7kAZBt2uzZCxvDHmwf6OYCnqd8NTrbDS3XyuHvV4qoZD",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "to": wa_id,
            "type": "text",
            "text": {
                "body": output
            }
        }

        response = requests.post(url, headers=headers, json=data)





    except (KeyError, IndexError) as e:
        print(f"Error accessing message body: {e}")
        # You can set body to None or handle the case however you want
        body = None









    return "OK", 200

if __name__ == "__main__":
    print(f"Starting server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=True)










