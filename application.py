

# import os
# import requests
# import flask
# from flask import Flask, request
# import logging
# from flask import Flask, request, jsonify

# import json
# import google.generativeai as genai
# from groq import Groq






# import os
# from flask import Flask, request

# port = int(os.environ.get('PORT', 4000))

# app = Flask(__name__)

# WEBHOOK_VERIFY_TOKEN = "HAPPY"

# def verify_webhook():
#     mode = request.args.get("hub.mode")
#     token = request.args.get("hub.verify_token")
#     challenge = request.args.get("hub.challenge")

#     print(f"Verification attempt - Mode: {mode}, Token: {token}, Challenge: {challenge}")

#     if mode == "subscribe" and token == WEBHOOK_VERIFY_TOKEN:
#         print("Webhook verified successfully!")
#         return str(challenge), 200
#     else:
#         print("Webhook verification failed.")
#         return '', 403


# # @app.route("/", methods=["GET"])
# # def root():
# #     if "hub.mode" in request.args:
# #         return verify_webhook()
# #     return "<p>Welcome to HTK API</p>"


# @app.route("/whatsapp", methods=["GET"])
# def whatsapp_verify():
#     # Assuming verify_webhook handles verification challenge from WhatsApp
#     return verify_webhook()





# app = Flask(__name__)

# # Define allowed display phone number and phone number ID
# ALLOWED_DISPLAY_PHONE_NUMBER = "2347070471117"
# ALLOWED_PHONE_NUMBER_ID = "396015606935687"

# @app.before_request
# def validate_request():
#     # Only run validation for POST requests to the /whatsapp endpoint
#     if request.method == "POST" and request.path == "/whatsapp":
#         try:
#             # Extract JSON payload from incoming request
#             data = request.get_json()
#             if not data:
#                 print("No JSON payload received.")
#                 return jsonify({"error": "Bad Request"}), 400

#             # Navigate through payload to extract phone number details
#             entry = data.get('entry', [])
#             if not entry:
#                 print("No entry in the payload.")
#                 return jsonify({"error": "Bad Request"}), 400
            
#             changes = entry[0].get('changes', [])
#             if not changes:
#                 print("No changes in the entry.")
#                 return jsonify({"error": "Bad Request"}), 400

#             value = changes[0].get('value', {})
#             metadata = value.get('metadata', {})
#             display_phone_number = metadata.get('display_phone_number')
#             phone_number_id = metadata.get('phone_number_id')

#             # Validate the incoming display phone number and phone number ID
#             if (display_phone_number != ALLOWED_DISPLAY_PHONE_NUMBER or 
#                 phone_number_id != ALLOWED_PHONE_NUMBER_ID):
#                 print(f"Rejected request from display number: {display_phone_number}, phone ID: {phone_number_id}")
#                 return jsonify({"error": "Forbidden"}), 403  # Reject the request early
            
#         except Exception as e:
#             print(f"Error during request validation: {e}")
#             return jsonify({"error": "Internal Server Error"}), 500


# MY_BUSINESS_PHONE_NUMBER = "2347070471117"





# @app.route("/whatsapp", methods=["POST"])

# def handle_incoming_message():

#     message = request.get_json()
#     print(message)
#     print("Processing message:", message)


#     body = message['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']

#     # Extract 'wa_id' from the contact
#     wa_id = message['entry'][0]['changes'][0]['value']['contacts'][0]['wa_id']

    
    
   
   
#     # Send response back to WhatsApp
#     url = "https://graph.facebook.com/v20.0/396015606935687/messages"
#     headers = {
#         "Authorization": "Bearer EAAPPDu1MMoEBO2TZAxphoxNidaagIIpn9ZCeq4nkv6gM61KVw5DrsnCY5zEGpZBAHPhc9IWfWx445fJLA1zOEyClbdvzDVwDOL6kehIy3UyWiQnJczV3M6QtOA3fLElalNhFVwjPnU5W6aCxnnM1ICeQSwdszAmcTsuxZAKJN54gvWJV0T1l0YZBNWzA5643U4eZB1SLr3ZClZCXWdZCy8VzgevvZCZBnxRk8EFZCsdAftMJX3MZD",
#         "Content-Type": "application/json"
#     }

#     data = {
#         "messaging_product": "whatsapp",
#         "to": wa_id,
#         "type": "text",
#         "text": {
#             "body": body
#         }
#     }

#     response = requests.post(url, headers=headers, json=data)




#     return "OK", 200

# if __name__ == "__main__":
#     print(f"Starting server on port {port}")
#     app.run(host='0.0.0.0', port=port, debug=True)













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
    # Extract text message and sender's number, ignore if conditions aren't met
    try:
        # Assuming 'messages' is present in the JSON structure
        entry = message.get('entry', [])
        
        if entry:
            changes = entry[0].get('changes', [])
            
            if changes:
                value = changes[0].get('value', {})
                messages = value.get('messages', [])
                contacts = value.get('contacts', [])

                if messages and contacts:
                    # Extract text body if it exists
                    if 'text' in messages[0] and 'body' in messages[0]['text']:
                        body = messages[0]['text']['body']
                        wa_id = contacts[0]['wa_id']


                        if body == "yes":

                            print("breakpoint")

                        else:
                            # File path for user history
                            history_file = f"user_{wa_id}_history.json"

                            # Check if user history exists
                            if os.path.exists(history_file):
                                with open(history_file, 'r') as f:
                                    chat_history = json.load(f)
                            else:
                                chat_history = []
                                chat_history.append({"role": "system", "content": "Your name is Prometheus and you help people especially women who have dreams and ideas to build their ideas. You are a like an assistant that can help women especially build websites and AI chatbots.  For now you can automatically create a simple one pager website for like a business, and you can create an AI chatbot and modify its behaviour. You are created to help people who have no technical expertise but still want to build great stuff.  That means the user will explain to you what they want and your job is to understand what your users want and just confirm with them."})

                            
                            from groq import Groq

                            # Add your API key here
                            api_key = "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"

                            # Instantiate the client with the API key
                            client = Groq(api_key=api_key)

                            # Store the output in a variable
                            output = ""

                            completion = client.chat.completions.create(
                                model="llama-3.2-11b-text-preview",
                                messages=
                                    chat_history
                        ,
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
                            print(output)
                            
                            # Update chat history
                            chat_history.append({"role": "user", "content": body})    # 'body' is a string
                            chat_history.append({"role": "assistant", "content": output})
                            print(chat_history)

                            # Save updated chat history
                            with open(history_file, 'w') as f:
                                json.dump(chat_history, f)


                            
                            # Send response back to WhatsApp
                            url = "https://graph.facebook.com/v20.0/396015606935687/messages"
                            headers = {
                                "Authorization": "Bearer EAAPPDu1MMoEBOzXqZCfroxXGYyono1AvwrkrTrg8OyhlH0KjTzqr9F5W36lvyZCV3fDoxpp92AgGnyKyRbt8ihOJ0za2PnsRJK3ZAhW4ZBoyeZBmzWKWAn9BZCouOQ9gghESIUG6xNxJlUJRlu6KwiQNHu7v3doZCCeKg8lN4qiPfCYZCcC0N5WVMmUqd2DYXir7EwZDZD",
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


                            chat_history.append({"role": "user", "content": "Based on your previous conversation with the user, what does the user want to build. 1. website or 2. AI chatbot 3. None. Reply with  1, 2 or 3 give no explanations. Only 1, 2, or 3"}) 
                            print("model is not giving the right reply")

                            from groq import Groq

                            # Add your API key here
                            api_key = "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"

                            # Instantiate the client with the API key
                            client = Groq(api_key=api_key)

                            # Store the output in a variable
                            output = ""

                            completion = client.chat.completions.create(
                                model="gemma-7b-it",
                                messages=
                                    chat_history
                        ,
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
                            print(output)


                            if output == "1":
                                
                                url = "https://graph.facebook.com/v20.0/396015606935687/messages"
                                headers = {
                                    "Authorization": "Bearer EAAPPDu1MMoEBOzXqZCfroxXGYyono1AvwrkrTrg8OyhlH0KjTzqr9F5W36lvyZCV3fDoxpp92AgGnyKyRbt8ihOJ0za2PnsRJK3ZAhW4ZBoyeZBmzWKWAn9BZCouOQ9gghESIUG6xNxJlUJRlu6KwiQNHu7v3doZCCeKg8lN4qiPfCYZCcC0N5WVMmUqd2DYXir7EwZDZD",
                                    "Content-Type": "application/json"
                                }

                                data = {
                                    "messaging_product": "whatsapp",
                                    "to": wa_id,
                                    "type": "text",
                                    "text": {
                                        "body": "Buiding has started... I will build your website as you instructed. When I'm done, I will send you the link to it."
                                    }
                                }

                                response = requests.post(url, headers=headers, json=data)






                   



                        


                    # No else case, just ignore if the text/body isn't present
    except (KeyError, IndexError) as e:
        pass  # Just ignore and do nothing
    
    return "OK", 200 




if __name__ == "__main__":
    print(f"Starting server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=True)










