

#https://healthtracka.com/

# import requests
# from bs4 import BeautifulSoup
# import urllib.parse

# def save_content(url, content, file):
#     file.write(f"URL: {url}\n")
#     file.write(content)
#     file.write("\n\n" + "="*80 + "\n\n")

# def scrape_page(url, visited, file):
#     if url in visited:
#         return
#     visited.add(url)
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         soup = BeautifulSoup(response.text, 'html.parser')
#         save_content(url, response.text, file)
#         print(f"Scraped {url}")
#         for link in soup.find_all('a', href=True):
#             next_url = urllib.parse.urljoin(url, link['href'])
#             if next_url.startswith(base_url):
#                 scrape_page(next_url, visited, file)
#     except requests.RequestException as e:
#         print(f"Failed to retrieve {url}: {e}")

# if __name__ == "__main__":
#     base_url = "https://healthtracka.com/"  # Replace with the website you want to scrape
#     visited = set()
#     with open("scraped_content.txt", 'w', encoding='utf-8') as file:
#         scrape_page(base_url, visited, file)



import requests
from bs4 import BeautifulSoup

url = "https://healthtracka.com/"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract specific data, for example, all the links on the page
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))

    # Extract other data based on your specific needs
    # For example, you could extract the title of the page:
    title = soup.find('title').text
    print(title)

else:
    print(f"Request failed with status code: {response.status_code}")






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
    genai.configure(api_key="AIzaSyDmX5Z5gwQ2v_Y696AjLRZgM0LyHNo91o4")

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
        system_instruction="You are the customer representative for this business\n\nSkip to content\n\n\nLAPRENGE STAFFINGS\nA Human Capital Company with a multi faceted structure in fields of Recruitment, Business Development and Management, Business Marketing, Human Resources consultancy, Training, Outsourcing,  and Verifications.\n\nLearn More\nWhat We Do\nAt laprenge Staffings , we are dedicated to giving you quality and exclusive service delivery that covers the above listed items…\n\nAbout Us\nRecruitment/Staffing\nWe specialize in connecting businesses with top talent, providing comprehensive recruitment and staffing solutions that drive success. Our expert team takes the time to understand your unique needs, sourcing and selecting the best candidates to fill your workforce gaps.\n\nBusiness Management\nAt Laprenge Staffings, we empower businesses to reach their full potential by providing expert management solutions. Our team takes a personalized approach to understand your unique needs, offering tailored support in areas such as strategy development, operations optimization and financial management.\n\nMentorship\nWe empower the next generation of business leaders to achieve their full potential. Our experienced mentors provide personalized guidance, sharing valuable insights and expertise to help you navigate the challenges of entrepreneurship. With a focus on strategic planning, leadership development, and industry expertise.\n\n\nA drive to innovative solutions!\nAll businesses need innovative solution with necessary human infrastructure to sustain her growth. THIS IS WHERE WE COME IN \n\nContact Us\nOur Mission\nTo through partnership Foaster excellent relationship between employer and employee to provide efficient, effective solutions through excellent delivery of service that promotes overall work place satisfaction resulting in customer satisfaction and retention for our business partners.\n\nOur Vission\nTo be the leading recruitment platform in Nigeria.\n\nWhatsApp Us\n\n[https://api.whatsapp.com/send?phone=2348167999713&text=Hy%20Laprenge%20Staffings%2C%20My%20name%20is..........................%20I%20need%20your%20services%20regarding........................................]\n\nA REMINDER\nAs a team, we don't compromise integrity and excellence.\n\nWhy Choose Us?\nSWIFT RESPONSE\nOur automated processes and team of experts ensures swift response for every request to help you make the best informed decisions without delay.\n\nPROFFESIONALS\nOur methodologies reflect a strict adherence to industry recognized standards. We provide innovative solutions that can be adapted to meet your company’s present needs.\n\nAFFORDABILITY\nOur Services are affordable. We easily fit into your budget always with our cost effective services. No hidden Charges at all and we offer you the best.\n\nCOMPLIANCE\nWe comply with regulatory requirements to enhance best practices and strengthen internal controls that protect the valuable reputation of your organization and employees.\n\nLaprenge Staffings is a Human Capital Company with a multi faceted structure in fields of Recruitment, Business Development and Management, Business Marketing, Human Resources consultancy, Training, Outsourcing, and Verifications.\n\n\n\nWe specialize in connecting businesses with top talent, providing comprehensive recruitment and staffing solutions that drive success.\n\nQuick Links\nHome\nAbout Us\nContact Us\nImportant Links\nTerms and Conditions\nLegal\nBusiness\nPartners\nLet’s Connect!\nConnect with our team let’s build your network, and make great business. This si the link to offically request a candidate [https://docs.google.com/forms/d/e/1FAIpQLSes1uZ145G-qKA-oN2t5S1bv0-vqdNmXeJLNALbs-NOY6Lb8Q/viewform]\n"
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
        "Authorization": "Bearer EAAPPDu1MMoEBOy8xa6fZAG8p7JJiDa3ZCX6pVT0qCKkZCENnCZAmdpLcVtbkeLOhINaRcV4NUvNHd3RZAdKnBFTNbgQ9CwaQP5rZBLeCpVeLIA6fv0AvoshJdm8IwTBiKbVBljKwXKVD3jZCmEdOfC9Gg5RumUJu41iQU3GaDZCxfUsZAsLYaVeyle25YWEOBwUsc5eT7kAZBt2uzZCxvDHmwf6OYCnqd8NTrbDS3XyuHvV4qoZD",
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

    if output  == "1":






    return "OK", 200

if __name__ == "__main__":
    print(f"Starting server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=True)



















import os
import requests
import flask
from flask import Flask, request
import logging
from flask import Flask, request, jsonify

import json
import google.generativeai as genai
from groq import Groq






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

    message = request.get_json()
    print(message)



     # Extract the list of messages if it exists
    if "messages" in message["entry"][0]["changes"][0]["value"]:
        body = message['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
        wa_id = message['entry'][0]['changes'][0]['value']['contacts'][0]['wa_id']


           
        # Send response back to WhatsApp
        url = "https://graph.facebook.com/v20.0/396015606935687/messages"
        headers = {
            "Authorization": "Bearer EAAPPDu1MMoEBO2TZAxphoxNidaagIIpn9ZCeq4nkv6gM61KVw5DrsnCY5zEGpZBAHPhc9IWfWx445fJLA1zOEyClbdvzDVwDOL6kehIy3UyWiQnJczV3M6QtOA3fLElalNhFVwjPnU5W6aCxnnM1ICeQSwdszAmcTsuxZAKJN54gvWJV0T1l0YZBNWzA5643U4eZB1SLr3ZClZCXWdZCy8VzgevvZCZBnxRk8EFZCsdAftMJX3MZD",
            "Content-Type": "application/json"
        }

        data = {
            "messaging_product": "whatsapp",
            "to": wa_id,
            "type": "text",
            "text": {
                "body": body
            }
        }

        response = requests.post(url, headers=headers, json=data)



    else:
        pass



    return "OK", 200

if __name__ == "__main__":
    print(f"Starting server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=True)










