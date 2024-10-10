

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
import google.generativeai as genai

global handled_messages
handled_messages = set()






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






                        if body in handled_messages:
                            print("breakpoint")
                            pass
                        else:
                            # File path for user history
                            history_file = f"user_{wa_id}_history.json"

                            # Check if user history exists
                            import os

                            if os.path.exists(history_file):
                                with open(history_file, 'r') as f:
                                    chat_history = json.load(f)
                            else:
                                chat_history = []
                                chat_history.append({"role": "system", "content": "Your name is Prometheus and you help people especially women who have dreams and ideas to build their ideas. You are a like an assistant that can help women especially build websites and AI chatbots.  For now you can automatically create a simple one pager website for like a business, and you can create an AI chatbot and modify its behaviour. You are created to help people who have no technical expertise but still want to build great stuff.  That means the user will explain to you what they want and your job is to understand what your user want and tell them what it would look like. Don't ask questions"})
                                chat_history.append({"role": "user", "content": body})


                            
                            from groq import Groq

                            # Add your API key here
                            api_key = "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"

                            # Instantiate the client with the API key
                            client = Groq(api_key=api_key)

                            # Store the output in a variable
                            model_output = ""

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
                                model_output += chunk.choices[0].delta.content or ""

                            # Now `output` holds the response from the model
                            print(model_output)
                            
                            # Update chat history
                            chat_history.append({"role": "user", "content": body})    # 'body' is a string
                            chat_history.append({"role": "assistant", "content": model_output})
                            #print(chat_history)

                            # Save updated chat history
                            with open(history_file, 'w') as f:
                                json.dump(chat_history, f)

                            import requests
                            
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
                                    "body": model_output
                                }
                            }

                            response = requests.post(url, headers=headers, json=data)
                            handled_messages.add(body)


                            chat_history.append({"role": "user", "content": "Based on your previous conversation with the user, what does the user want to build. 1. website or 2. AI chatbot 3. None. Reply with  1, 2 or 3 give no explanations. Only 1, 2, or 3. Reply with 1 2 or 3, nothing else just the numbers"}) 
                            print("model is not giving the right reply")

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


                            if output == "1":
                                import requests

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


                                from googlesearch import search
                                from bs4 import BeautifulSoup
                                import requests




                                chat_history.append({"role": "user", "content": f"reply with one word, pictures of what should be on the website that this person wants to build? this s the user's input: {body}"})
                            
                                from groq import Groq

                                # Add your API key here
                                api_key = "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"

                                # Instantiate the client with the API key
                                client = Groq(api_key=api_key)

                                # Store the output in a variable
                                query = ""

                                completion = client.chat.completions.create(
                                    model="llama-3.2-11b-text-preview",
                                    messages=
                                        chat_history,
                                    temperature=1,
                                    max_tokens=1024,
                                    top_p=1,
                                    stream=True,
                                    stop=None,
                                )

                                # Append the output to the variable
                                for chunk in completion:
                                    query += chunk.choices[0].delta.content or ""

                                # Now `output` holds the response from the model
                                print(query)




                                
                                import requests

                                def get_image_links(query, access_key, num_links=10):
                                    image_links = []
                                    # Construct the API request
                                    url = f"https://api.unsplash.com/search/photos/?client_id={access_key}&query={query}&per_page={num_links}"
                                    # Send the request
                                    response = requests.get(url)
                                    # Parse the JSON response
                                    data = response.json()
                                    # Extract image links
                                    for result in data["results"]:
                                        image_links.append(result["urls"]["full"])
                                    return image_links

                                # Example usage:
                                object_query =  query
                                access_key = "Zms9L2hVgdrmWDsLQ4SqLVI34NbSEnh3oG_xTVl5GW0"
                                image_links = get_image_links(object_query, access_key)
                                print(image_links)
                                # for link in image_links:
                                #     print(link)
                                    
                                import requests


                                #keeping user in loop
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
                                        "body": "I just finished downloading the images for your website, I am moving to coding now..."
                                    }
                                }

                                response = requests.post(url, headers=headers, json=data)




                            #     chat_history = []
                            #     chat_history.append({"role": "system", "content": f"You are the best html website coder ever, you take a description of the website to build and you only reply with the detailed and complete html code to implement it. Here is the image url. I have the js file called script.js and css file called style.css files. Don't bother about them, focus on making the html as extensive and good as possible. Do not use external apis right now. Reply only with the html code, give no explanations.  Here are the image links to use in the builiding {image_links}"})
                            #     chat_history.append({"role": "user", "content": body})


                            
                            #     from groq import Groq

                            #     # Add your API key here
                            #     api_key = "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"

                            #     # Instantiate the client with the API key
                            #     client = Groq(api_key=api_key)

                            #     # Store the output in a variable
                            #     html_output = ""

                            #     completion = client.chat.completions.create(
                            #         model="llama-3.2-11b-text-preview",
                            #         messages=
                            #             chat_history
                            # ,
                            #         temperature=1,
                            #         max_tokens=1024,
                            #         top_p=1,
                            #         stream=True,
                            #         stop=None,
                            #     )

                            #     # Append the output to the variable
                            #     for chunk in completion:
                            #         html_output += chunk.choices[0].delta.content or ""

                                
                                import google.generativeai as genai
                                genai.configure(api_key="AIzaSyD3M4VzknhIcd-ikyA9P4LXiLEoSjH1JQ8")

                                # Set up the model
                                generation_config = {
                                "temperature": 0.9,
                                "top_p": 1,
                                "top_k": 1,
                                "max_output_tokens": 4048,
                                }

                                safety_settings = [
                                {
                                    "category": "HARM_CATEGORY_HARASSMENT",
                                    "threshold": "BLOCK_NONE"
                                },
                                {
                                    "category": "HARM_CATEGORY_HATE_SPEECH",
                                    "threshold": "BLOCK_NONE"
                                },
                                {
                                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                                    "threshold": "BLOCK_NONE"
                                },
                                {
                                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                                    "threshold": "BLOCK_NONE"
                                },
                                ]

                                model = genai.GenerativeModel(model_name="gemini-1.5-flash-002",
                                                            generation_config=generation_config,
                                                            safety_settings=safety_settings)

                                convo = model.start_chat(history=[
                                ])

                                convo.send_message(f"create the HTML part of this project{model_output} and I have image links that you must use in the wesbite here {image_links}. i have js called script.js and css called style.css files. Make sure the website is professional. use the image links, i gave you. Make the website robust and well detailed. Generate the website content too. Give no explanations,  just give me the code")
                                html_content = convo.last.text
                                html_output = html_content

                                # Now `output` holds the response from the model
                                print(html_output)


                            #     chat_history = []
                            #     chat_history.append({"role": "system", "content": f"You are the best css website coder ever, you take the html code {html_output} of the website we're building and write the css code to make it beautiful and you only reply with the detailed and complete css code to implement it. Here is the html code. I have the js file called script.js  Don't bother about it, focus on making the css as extensive and good as possible. Reply only with the css code, give no explanations."})
                            #     chat_history.append({"role": "user", "content": "make the css compliment our website very well. make it look very nice and professional. Reply only with css code, do not give any explanations. Make the css code extensive."})


                            
                            #     from groq import Groq

                            #     # Add your API key here
                            #     api_key = "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"

                            #     # Instantiate the client with the API key
                            #     client = Groq(api_key=api_key)

                            #     # Store the output in a variable
                            #     css_output = ""

                            #     completion = client.chat.completions.create(
                            #         model="llama-3.2-11b-text-preview",
                            #         messages=
                            #             chat_history
                            # ,
                            #         temperature=1,
                            #         max_tokens=1024,
                            #         top_p=1,
                            #         stream=True,
                            #         stop=None,
                            #     )

                            #     # Append the output to the variable
                            #     for chunk in completion:
                            #         css_output += chunk.choices[0].delta.content or ""

                            #     # Now `output` holds the response from the model
                            #     print(css_output)


                                import google.generativeai as genai

                                genai.configure(api_key="AIzaSyD3M4VzknhIcd-ikyA9P4LXiLEoSjH1JQ8")

                                # Set up the model
                                generation_config = {
                                "temperature": 0.9,
                                "top_p": 1,
                                "top_k": 1,
                                "max_output_tokens": 2048,
                                }

                                safety_settings = [
                                {
                                    "category": "HARM_CATEGORY_HARASSMENT",
                                    "threshold": "BLOCK_NONE"
                                },
                                {
                                    "category": "HARM_CATEGORY_HATE_SPEECH",
                                    "threshold": "BLOCK_NONE"
                                },
                                {
                                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                                    "threshold": "BLOCK_NONE"
                                },
                                {
                                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                                    "threshold": "BLOCK_NONE"
                                },
                                ]

                                model = genai.GenerativeModel(model_name="gemini-1.5-flash-002",
                                                            generation_config=generation_config,
                                                            safety_settings=safety_settings)

                                convo = model.start_chat(history=[
                                ])

                                convo.send_message(f"generating code only, create the CSS PART of this project{model_output}, considering this is the html part {html_output} feel free to be creative, make sure the website is well designed and the displays professioanlism. Give no explanations, just pure code. Make it look good, please and have an hero segment")
                                css_content = convo.last.text
                                css_output = css_content
                                print(css_content)





                                import google.generativeai as genai

                                genai.configure(api_key="AIzaSyD3M4VzknhIcd-ikyA9P4LXiLEoSjH1JQ8")

                                # Set up the model
                                generation_config = {
                                "temperature": 0.9,
                                "top_p": 1,
                                "top_k": 1,
                                "max_output_tokens": 2048,
                                }

                                safety_settings = [
                                {
                                    "category": "HARM_CATEGORY_HARASSMENT",
                                    "threshold": "BLOCK_NONE"
                                },
                                {
                                    "category": "HARM_CATEGORY_HATE_SPEECH",
                                    "threshold": "BLOCK_NONE"
                                },
                                {
                                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                                    "threshold": "BLOCK_NONE"
                                },
                                {
                                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                                    "threshold": "BLOCK_NONE"
                                },
                                ]

                                model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                                                            generation_config=generation_config,
                                                            safety_settings=safety_settings)

                                convo = model.start_chat(history=[
                                ])

                                convo.send_message(f"genating code only, create the JS PART of this project{model_output}, considering this is the html part {html_output} feel free to be creative, make sure the website is well designed and the displays professioanlism. Give no explanations, just pure code")
                                js_output = convo.last.text
                                js_content = js_output







                            #     chat_history = []
                            #     chat_history.append({"role": "system", "content": f"You are the best js website coder ever, you take the html code {html_output} of the website we're building and write the js code to make it beautiful and well made and you only reply with the detailed and complete js code to implement it. Here is the html code. Reply only with the js code, give no explanations."})
                            #     chat_history.append({"role": "user", "content": "make the js compliment our website very well. make it look very nice and professional. Reply only with js code, do not give any explanations. Make the js code extensive."})


                            #     from groq import Groq

                            #     # Add your API key here
                            #     api_key = "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"

                            #     # Instantiate the client with the API key
                            #     client = Groq(api_key=api_key)

                            #     # Store the output in a variable
                            #     js_output = ""

                            #     completion = client.chat.completions.create(
                            #         model="llama-3.2-11b-text-preview",
                            #         messages=
                            #             chat_history
                            # ,
                            #         temperature=1,
                            #         max_tokens=1024,
                            #         top_p=1,
                            #         stream=True,
                            #         stop=None,
                            #     )

                            #     # Append the output to the variable
                            #     for chunk in completion:
                            #         js_output += chunk.choices[0].delta.content or ""

                            #     # Now `output` holds the response from the model
                            #     print(js_output)



                                import requests


                                #keeping user in loop
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
                                        "body": "I have generated the code, now deploying...."
                                    }
                                }

                                response = requests.post(url, headers=headers, json=data)




                                # Create directories for files if they don't exist
                                os.makedirs("website", exist_ok=True)

                                # Write HTML content to a file
                                with open("website/index.html", "w") as html_file:
                                    html_file.write(html_output)

                                # Write CSS content to a file
                                with open("website/style.css", "w") as css_file:
                                    css_file.write(css_output)

                                # Write JavaScript content to a file
                                with open("website/script.js", "w") as js_file:
                                    js_file.write(js_output)


                                deploy_url = ""

                                import requests
                                # Netlify API endpoint
                                NETLIFY_API = "https://api.netlify.com/api/v1"

                                def deploy_to_netlify(access_token, directory_path, site_name=None):
                                    # Validate the directory
                                    if not os.path.isdir(directory_path):
                                        raise ValueError(f"The specified path '{directory_path}' is not a valid directory.")

                                    # Prepare the headers for the API request
                                    headers = {
                                        "Authorization": f"Bearer {access_token}",
                                        "Content-Type": "application/zip"
                                    }

                                    # Zip the directory
                                    zip_path = "site.zip"
                                    os.system(f"zip -r {zip_path} {directory_path}")

                                    # Create a new site if site_name is provided
                                    if site_name:
                                        import requests
                                        create_site_response = requests.post(
                                            f"{NETLIFY_API}/sites",
                                            headers=headers,
                                            json={"name": site_name}
                                        )
                                        if create_site_response.status_code != 201:
                                            print(f"Failed to create site. Status code: {create_site_response.status_code}")
                                            print(f"Error message: {create_site_response.text}")
                                            return
                                        site_id = create_site_response.json()["id"]
                                        print(f"Created new site with ID: {site_id}")
                                    else:
                                        # If no site_name is provided, deploy to the user's first site
                                        sites_response = requests.get(f"{NETLIFY_API}/sites", headers=headers)
                                        if sites_response.status_code != 200 or not sites_response.json():
                                            print("No existing sites found and no site name provided to create a new one.")
                                            return
                                        site_id = sites_response.json()[0]["id"]
                                        print(f"Deploying to existing site with ID: {site_id}")

                                    # Upload the zipped site
                                    with open(zip_path, "rb") as zip_file:
                                        response = requests.post(
                                            f"{NETLIFY_API}/sites/{site_id}/deploys",
                                            headers=headers,
                                            data=zip_file
                                        )

                                    # Clean up the zip file
                                    os.remove(zip_path)

                                    # Check the response
                                    if response.status_code == 200:
                                        deploy_url = response.json()["deploy_url"]
                                        print(f"Deployment successful! Your site is live at: {deploy_url}")

                                         #keeping user in loop
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
                                                "body": deploy_url
                                            }
                                        }



                                        import requests

                                        response = requests.post(url, headers=headers, json=data)
                                          # Open the URL in the default web browser
                                    else:
                                        print(f"Deployment failed. Status code: {response.status_code}")
                                        print(f"Error message: {response.text}")

                                # Usage
                                access_token = "nfp_4uUmEKzfAsAa1dmVYedSeebLDEw6DKmT49a8"
                                directory_path = "website"
                                site_name = "my-awesome-site"  # Optional: Provide a name to create a new site



                                deploy_to_netlify(access_token, directory_path, site_name)
                                chat_history = []




                                
                            elif output == "2":
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
                                        "body": "Sure, I will build that for you. Initiating building process..."
                                    }
                                }
                                import requests
                                response = requests.post(url, headers=headers, json=data)



                                import os
                                import google.generativeai as genai

                                genai.configure(api_key="AIzaSyD3M4VzknhIcd-ikyA9P4LXiLEoSjH1JQ8")

                                # Create the model
                                generation_config = {
                                "temperature": 1,
                                "top_p": 0.95,
                                "top_k": 40,
                                "max_output_tokens": 8192,
                                "response_mime_type": "text/plain",
                                }

                                model = genai.GenerativeModel(
                                model_name="gemini-1.5-flash-002",
                                generation_config=generation_config,
                                # safety_settings = Adjust safety settings
                                # See https://ai.google.dev/gemini-api/docs/safety-settings
                                system_instruction="edit only the ui of this chatbot, this is our template, follow this, chnage the color or font type or ai greeting, dont add anything to the logic. Reply only with code with no explanations. Replace the simulated response with the bot's description of it self\n\n<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\" />\n    <link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/css?family=Montserrat:400,700&display=swap\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />\n    <title>Chat Interface</title>\n    <style>\n        :root {\n            font-family: 'Montserrat', sans-serif;\n            font-size: 16px;\n            line-height: 24px;\n            color: #0f0f0f;\n            background-color: #f6f6f6;\n        }\n\n        body {\n            margin: 0;\n            padding: 0;\n            height: 100vh;\n            display: flex;\n            flex-direction: column;\n        }\n\n        .chat-container {\n            display: flex;\n            flex-direction: column;\n            height: 100vh;\n            max-width: 1200px;\n            margin: 0 auto;\n            width: 100%;\n            padding: 20px;\n            box-sizing: border-box;\n        }\n\n        .chat-header {\n            text-align: center;\n            padding: 20px 0;\n            border-bottom: 1px solid #eaeaea;\n        }\n\n        .chat-header h1 {\n            background: linear-gradient(to right, #00ffff, #cf23cf);\n            -webkit-background-clip: text;\n            -webkit-text-fill-color: transparent;\n            margin: 0;\n            padding: 0;\n            font-size: 2.5rem;\n        }\n\n        .chat-messages {\n            flex-grow: 1;\n            overflow-y: auto;\n            padding: 20px 0;\n            display: flex;\n            flex-direction: column;\n            gap: 20px;\n        }\n\n        .message {\n            max-width: 80%;\n            padding: 12px 16px;\n            border-radius: 12px;\n            margin: 4px 0;\n        }\n\n        .user-message {\n            align-self: flex-end;\n            background-color: #646cff;\n            color: white;\n        }\n\n        .assistant-message {\n            align-self: flex-start;\n            background-color: #f0f0f0;\n            color: #333;\n        }\n\n        .chat-input-container {\n            padding: 20px 0;\n            border-top: 1px solid #eaeaea;\n            display: flex;\n            gap: 10px;\n        }\n\n        .chat-input {\n            flex-grow: 1;\n            padding: 12px;\n            border: 1px solid #ddd;\n            border-radius: 8px;\n            font-family: inherit;\n            font-size: 1rem;\n            outline: none;\n            transition: border-color 0.2s;\n        }\n\n        .chat-input:focus {\n            border-color: #646cff;\n        }\n\n        .send-button {\n            padding: 12px 24px;\n            background-color: #646cff;\n            color: white;\n            border: none;\n            border-radius: 8px;\n            cursor: pointer;\n            transition: background-color 0.2s;\n        }\n\n        .send-button:hover {\n            background-color: #535bf2;\n        }\n\n        .loading-spinner {\n            width: 25px;\n            height: 25px;\n            border: 3px solid #f0f0f0;\n            border-top: 3px solid #646cff;\n            border-radius: 50%;\n            animation: spin 1s linear infinite;\n            margin: 20px auto;\n            display: none;\n        }\n\n        @keyframes spin {\n            0% { transform: rotate(0deg); }\n            100% { transform: rotate(360deg); }\n        }\n\n        @media (prefers-color-scheme: dark) {\n            :root {\n                color: #f6f6f6;\n                background-color: #1a1a1a;\n            }\n\n            .chat-header {\n                border-bottom-color: #333;\n            }\n\n            .chat-input-container {\n                border-top-color: #333;\n            }\n\n            .chat-input {\n                background-color: #2a2a2a;\n                border-color: #444;\n                color: white;\n            }\n\n            .assistant-message {\n                background-color: #2a2a2a;\n                color: #f6f6f6;\n            }\n        }\n    </style>\n</head>\n<body>\n    <div class=\"chat-container\">\n        <div class=\"chat-header\">\n            <h1>Chat Interface</h1>\n        </div>\n        \n        <div class=\"chat-messages\" id=\"chat-messages\">\n            <div class=\"message assistant-message\">\n                Hello! How can I help you today?\n            </div>\n        </div>\n\n        <div id=\"loadingSpinner\" class=\"loading-spinner\"></div>\n\n        <div class=\"chat-input-container\">\n            <input \n                type=\"text\" \n                class=\"chat-input\" \n                id=\"chat-input\" \n                placeholder=\"Type your message here...\"\n            >\n            <button class=\"send-button\" id=\"send-button\">Send</button>\n        </div>\n    </div>\n\n    <script>\n        const chatInput = document.getElementById('chat-input');\n        const sendButton = document.getElementById('send-button');\n        const chatMessages = document.getElementById('chat-messages');\n        const loadingSpinner = document.getElementById('loadingSpinner');\n\n        function addMessage(message, isUser = false) {\n            const messageDiv = document.createElement('div');\n            messageDiv.className = `message ${isUser ? 'user-message' : 'assistant-message'}`;\n            messageDiv.textContent = message;\n            chatMessages.appendChild(messageDiv);\n            chatMessages.scrollTop = chatMessages.scrollHeight;\n        }\n\n        function handleSend() {\n            const message = chatInput.value.trim();\n            if (message) {\n                addMessage(message, true);\n                chatInput.value = '';\n                \n                // Show loading spinner\n                loadingSpinner.style.display = 'block';\n                \n                // Simulate response (replace with actual API call)\n                setTimeout(() => {\n                    loadingSpinner.style.display = 'none';\n                    \n                    addMessage('This is a simulated response. Replace with actual API integration.');\n                }, 1000);\n            }\n        }\n\n        sendButton.addEventListener('click', handleSend);\n        chatInput.addEventListener('keypress', (e) => {\n            if (e.key === 'Enter') {\n                handleSend();\n            }\n        });\n    </script>\n</body>\n</html>",
                                )

                                chat_session = model.start_chat(
                                history=[
                                ]
                                )

                                response = chat_session.send_message(body)

                                bot_code = response.text
                                print(bot_code)

                                # Create directories for files if they don't exist
                                os.makedirs("bot_website", exist_ok=True)

                                # Write HTML content to a file
                                with open("website_bot/index.html", "w") as html_file:
                                    html_file.write(bot_code)


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
                                        "body": "Building complete, starting deployment..."
                                    }
                                }

                                import requests

                                response = requests.post(url, headers=headers, json=data)



                                import requests
                                # Netlify API endpoint
                                NETLIFY_API = "https://api.netlify.com/api/v1"

                                def deploy_to_netlify(access_token, directory_path, site_name=None):
                                    # Validate the directory
                                    if not os.path.isdir(directory_path):
                                        raise ValueError(f"The specified path '{directory_path}' is not a valid directory.")

                                    # Prepare the headers for the API request
                                    headers = {
                                        "Authorization": f"Bearer {access_token}",
                                        "Content-Type": "application/zip"
                                    }

                                    # Zip the directory
                                    zip_path = "site.zip"
                                    os.system(f"zip -r {zip_path} {directory_path}")

                                    # Create a new site if site_name is provided
                                    if site_name:
                                        import requests
                                        create_site_response = requests.post(
                                            f"{NETLIFY_API}/sites",
                                            headers=headers,
                                            json={"name": site_name}
                                        )
                                        if create_site_response.status_code != 201:
                                            print(f"Failed to create site. Status code: {create_site_response.status_code}")
                                            print(f"Error message: {create_site_response.text}")
                                            return
                                        site_id = create_site_response.json()["id"]
                                        print(f"Created new site with ID: {site_id}")
                                    else:
                                        # If no site_name is provided, deploy to the user's first site
                                        sites_response = requests.get(f"{NETLIFY_API}/sites", headers=headers)
                                        if sites_response.status_code != 200 or not sites_response.json():
                                            print("No existing sites found and no site name provided to create a new one.")
                                            return
                                        site_id = sites_response.json()[0]["id"]
                                        print(f"Deploying to existing site with ID: {site_id}")

                                    # Upload the zipped site
                                    with open(zip_path, "rb") as zip_file:
                                        response = requests.post(
                                            f"{NETLIFY_API}/sites/{site_id}/deploys",
                                            headers=headers,
                                            data=zip_file
                                        )

                                    # Clean up the zip file
                                    os.remove(zip_path)

                                    # Check the response
                                    if response.status_code == 200:
                                        deploy_url = response.json()["deploy_url"]
                                        print(f"Deployment successful! Your site is live at: {deploy_url}")

                                         #keeping user in loop
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
                                                "body": deploy_url
                                            }
                                        }



                                        import requests

                                        response = requests.post(url, headers=headers, json=data)
                                          # Open the URL in the default web browser
                                    else:
                                        print(f"Deployment failed. Status code: {response.status_code}")
                                        print(f"Error message: {response.text}")

                                # Usage
                                access_token = "nfp_4uUmEKzfAsAa1dmVYedSeebLDEw6DKmT49a8"
                                directory_path = "website_bot"
                                site_name = "my-awesome-site"  # Optional: Provide a name to create a new site

                                deploy_to_netlify(access_token, directory_path, site_name)
                                chat_history = []

                                

            
                    # No else case, just ignore if the text/body isn't present
    except (KeyError, IndexError) as e:
        pass  # Just ignore and do nothing
    
    return "OK", 200 




if __name__ == "__main__":
    print(f"Starting server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=True)










