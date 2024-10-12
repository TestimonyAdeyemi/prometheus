

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




                                chat_history.append({"role": "user", "content": f"reply with a search query, pictures of what should be on the website that this person wants to build? What should i search for? this the user's input: {body}"})
                            
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

                                chat_history = []




                                
                                import requests

                                def get_image_links(query, access_key, num_links=5):
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
                                for link in image_links:
                                    print(link)


                                import requests
                                from bs4 import BeautifulSoup
                                import re

                                def get_image_urls(query, num_images=10):
                                    # Format the query to be URL-safe
                                    query = query.replace(' ', '+')
                                    url = f"https://www.google.com/search?q={query}&tbm=isch"

                                    # Set up headers to mimic a regular browser request
                                    headers = {
                                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
                                    }

                                    # Send the request to Google
                                    response = requests.get(url, headers=headers)
                                    if response.status_code != 200:
                                        print("Failed to retrieve data")
                                        return []

                                    # Parse the HTML content using BeautifulSoup
                                    soup = BeautifulSoup(response.text, 'html.parser')

                                    # Find all image elements
                                    image_elements = soup.find_all("img", {"src": re.compile("gstatic.com")})
                                    
                                    # Extract image URLs
                                    image_urls = [img["src"] for img in image_elements[:num_images]]

                                    return image_urls

                                # Example usage:
                                search_query = query
                                image_urls = get_image_urls(search_query)

                                # Display the image URLs
                                print("Image URLs:", image_urls)

                                image_links = image_urls


                                #image_links = "['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTR3zygyl9qt5xYRbKO_tMhIM9k0giUt3fCjTuWg2bcopGYaoEf_Agn52nZEfE&s', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREB24jgWEQnzMDhORw_XJz-38U3pNaRKl6voHUybEd2RqO34lyZrmb2lI5Ig&s', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFFBJKHxGhNWi_NssWOfpGPiglJ-nvZhJVLi2mt8pPjkeSLVpY3dzfbk9lwg&s', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnJxKytCmMrp6z24RT5rcUPuDAXSzoJ2N7xdpD5zGAgq4rJUR-6cay-QQgcUM&s', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPjpeCMFjjvOrAdSLFeY82ASEV5-c2GVcpijFzhBkbaWUiCz3K1gQeB0KiI2I&s', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2mD-wIxNnLW8z_1WoIaEIkSjHwgVriXQaRMFp-LwQWH-89oHo6LAgAQWelQ&s', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwp4IILc3OVlhw6wD3brwnRyb1egNq4fWkGrHsxYyK1qD6nroRZFwpX33z-Q&s', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQI_qzKjg2Vr_ThUw8-d0tHeR0jn9Ge4RBQpGifKwOm26h0JQtURmfbs6Fd9iA&s', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgBVtDFhijOs574noueTOJO0J0Wrz1-jIoC6Vh7PXHfG0oaKrMLphvYVrSzQ&s', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQKhVdqmVxFlvnN5icheRunry-iACXJe86co6Jqdlx0TkuJQ4a2IVaPtgZpA&s']"







                                    







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

                                inspiration = "<!DOCTYPE html>\n<html lang=\"en\">\n  <head>\n    <meta charset=\"UTF-8\" />\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />\n    <link\n      href=\"https://cdn.jsdelivr.net/npm/remixicon@4.2.0/fonts/remixicon.css\"\n      rel=\"stylesheet\"\n    />\n    <title>Web Design Mastery | Burger House</title>\n    <style>\n      @import url(\"https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Bebas+Neue&family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap\");\n\n      :root {\n        --primary-color: #42200b;\n        --secondary-color: #ffc135;\n        --tertiary-color: #df1c1c;\n        --text-dark: #212529;\n        --white: #ffffff;\n        --max-width: 1200px;\n        --header-font-1: \"Alfa Slab One\", serif;\n        --header-font-2: \"Bebas Neue\", sans-serif;\n      }\n\n      * {\n        padding: 0;\n        margin: 0;\n        box-sizing: border-box;\n      }\n\n      .section__container {\n        max-width: var(--max-width);\n        margin: auto;\n        padding: 5rem 1rem;\n      }\n\n      .section__header {\n        font-size: 3rem;\n        font-weight: 500;\n        font-family: var(--header-font-1);\n        color: var(--primary-color);\n        text-align: center;\n        line-height: 3.75rem;\n        text-shadow: 2px 2px var(--secondary-color);\n      }\n\n      .section__description {\n        font-weight: 500;\n        color: var(--text-dark);\n        line-height: 1.75rem;\n      }\n\n      .btn {\n        padding: 1rem 1.5rem;\n        outline: none;\n        border: none;\n        font-size: 1rem;\n        color: var(--white);\n        background-color: var(--tertiary-color);\n        transition: 0.3s;\n        cursor: pointer;\n      }\n\n      .btn:hover {\n        background-color: var(--primary-color);\n      }\n\n      img {\n        display: flex;\n        width: 100%;\n      }\n\n      a {\n        text-decoration: none;\n        transition: 0.3s;\n      }\n\n      html,\n      body {\n        scroll-behavior: smooth;\n      }\n\n      body {\n        font-family: \"Montserrat\", sans-serif;\n      }\n\n      .header {\n        background-image: url(\"assets/header-bg.png\");\n        background-position: center center;\n        background-size: cover;\n        background-repeat: no-repeat;\n      }\n\n      nav {\n        position: fixed;\n        width: 100%;\n        max-width: var(--max-width);\n        margin-inline: auto;\n        z-index: 9;\n      }\n\n      .nav__header {\n        padding: 1rem;\n        display: flex;\n        align-items: center;\n        justify-content: space-between;\n        background-color: var(--primary-color);\n      }\n\n      .nav__logo img {\n        max-width: 150px;\n      }\n\n      .nav__logo-dark {\n        display: none;\n      }\n\n      .nav__menu__btn {\n        font-size: 1.5rem;\n        color: var(--white);\n        cursor: pointer;\n      }\n\n      .nav__links {\n        position: absolute;\n        top: 60px;\n        left: 0;\n        width: 100%;\n        padding: 2rem;\n        list-style: none;\n        display: flex;\n        align-items: center;\n        justify-content: center;\n        flex-direction: column;\n        gap: 2rem;\n        background-color: var(--primary-color);\n        transition: 0.5s;\n        z-index: -1;\n        transform: translateY(-100%);\n      }\n\n      .nav__links.open {\n        transform: translateY(0);\n      }\n\n      .nav__links a {\n        font-weight: 600;\n        white-space: nowrap;\n        color: var(--white);\n        transition: 0.3s;\n      }\n\n      .nav__links a:hover {\n        color: var(--secondary-color);\n      }\n\n      .header__container {\n        display: grid;\n        gap: 2rem;\n        overflow: hidden;\n      }\n\n      .header__image img {\n        max-width: 600px;\n        margin-inline: auto;\n      }\n\n      .header__content h2 {\n        max-width: 400px;\n        margin-inline: auto;\n        margin-bottom: 2rem;\n        padding: 1rem 2rem;\n        font-size: 1.75rem;\n        font-weight: 400;\n        font-family: var(--header-font-2);\n        color: var(--primary-color);\n        border: 2px dashed var(--primary-color);\n        text-align: center;\n      }\n\n      .header__content h1 {\n        font-size: 4.5rem;\n        font-weight: 500;\n        font-family: var(--header-font-1);\n        color: var(--primary-color);\n        line-height: 3.5rem;\n        text-align: center;\n        text-shadow: 2px 2px var(--white);\n      }\n\n      .header__content h1 span {\n        font-size: 3rem;\n      }\n\n      .banner__container {\n        display: grid;\n        gap: 1rem;\n        grid-auto-rows: 200px;\n      }\n\n      .banner__card {\n        padding: 1rem;\n        background-position: center center;\n        background-size: cover;\n        background-repeat: no-repeat;\n        border-radius: 1rem;\n      }\n\n      .banner__card:nth-child(1) {\n        background-image: url(\"assets/banner-1.png\");\n      }\n\n      .banner__card:nth-child(2) {\n        background-image: url(\"assets/banner-2.png\");\n      }\n\n      .banner__card:nth-child(3) {\n        background-image: url(\"assets/banner-3.png\");\n      }\n\n      .banner__card p {\n        margin-bottom: 0.5rem;\n        font-size: 1.5rem;\n        font-weight: 500;\n        color: var(--white);\n      }\n\n      .banner__card h4 {\n        font-size: 2rem;\n        font-weight: 600;\n        color: var(--white);\n      }\n\n      .order__container h3 {\n        max-width: fit-content;\n        margin-inline: auto;\n        margin-bottom: 1rem;\n        padding: 0.5rem 2rem;\n        font-size: 1.5rem;\n        font-weight: 400;\n        font-family: var(--header-font-2);\n        color: var(--primary-color);\n        background-color: var(--secondary-color);\n      }\n\n      .order__container .section__header {\n        margin-bottom: 1rem;\n      }\n\n      .order__container .section__description {\n        margin-bottom: 2rem;\n        text-align: center;\n      }\n\n      .order__grid {\n        display: grid;\n        gap: 2rem 1rem;\n      }\n\n      .order__card {\n        padding: 2rem 1rem;\n        border-radius: 1rem;\n        text-align: center;\n        transition: 0.3s;\n      }\n\n      .order__card:hover {\n        box-shadow: 5px 5px 30px rgba(0, 0, 0, 0.1);\n      }\n\n      .order__card img {\n        max-width: 250px;\n        margin-inline: auto;\n        margin-bottom: 2rem;\n        filter: drop-shadow(10px 10px 30px rgba(0, 0, 0, 0.3));\n      }\n\n      .order__card h4 {\n        margin-bottom: 1rem;\n        font-size: 1.5rem;\n        font-weight: 600;\n        color: var(--text-dark);\n      }\n\n      .order__card p {\n        margin-bottom: 2rem;\n        font-weight: 500;\n        color: var(--text-dark);\n        line-height: 1.75rem;\n      }\n\n      .event__content {\n        display: grid;\n        gap: 2rem;\n        padding: 1rem;\n        box-shadow: 5px 5px 20px rgba(0, 0, 0, 0.1);\n      }\n\n      .event__details {\n        text-align: center;\n      }\n\n      .event__details h3 {\n        font-size: 2rem;\n        font-weight: 500;\n        font-family: var(--header-font-2);\n        color: var(--text-dark);\n      }\n\n      .event__details .section__header {\n        margin-bottom: 1rem;\n      }\n\n      .reservation {\n        position: relative;\n        isolation: isolate;\n      }\n\n      .reservation__container h3 {\n        font-size: 2rem;\n        font-weight: 500;\n        font-family: var(--header-font-2);\n        color: var(--text-dark);\n        text-align: center;\n      }\n\n      .reservation__container form {\n        max-width: 400px;\n        margin-inline: auto;\n        margin-top: 4rem;\n        display: grid;\n        gap: 1rem;\n      }\n\n      .reservation__container input {\n        padding: 0.75rem 1rem;\n        outline: none;\n        border: 1px solid var(--text-dark);\n        font-size: 1rem;\n        color: var(--text-dark);\n      }\n\n      .reservation__container input::placeholder {\n        color: var(--text-dark);\n      }\n\n      .reservation img {\n        display: none;\n      }\n\n      .footer {\n        background-image: url(\"assets/footer-bg.png\");\n        background-position: center center;\n        background-size: cover;\n        background-repeat: no-repeat;\n      }\n\n      .footer__logo img {\n        max-width: 250px;\n      }\n\n      .footer__content {\n        margin-top: 2rem;\n        display: grid;\n        gap: 2rem;\n      }\n\n      .footer__content p {\n        font-weight: 5500;\n        color: var(--white);\n        line-height: 1.75rem;\n      }\n\n      .footer__links {\n        list-style: none;\n        display: grid;\n        gap: 1rem;\n      }\n\n      .footer__links li {\n        display: flex;\n        align-items: center;\n        gap: 1rem;\n        font-weight: 500;\n        color: var(--white);\n      }\n\n      .footer__links li span {\n        font-size: 1.25rem;\n      }\n\n      .footer__socials {\n        margin-top: 2rem;\n        display: flex;\n        align-items: center;\n        gap: 1rem;\n      }\n\n      .footer__socials a {\n        font-size: 1.5rem;\n        color: var(--white);\n      }\n\n      .footer__socials a:hover {\n        color: var(--secondary-color);\n      }\n\n      .footer__bar {\n        padding: 1rem;\n        font-size: 0.9rem;\n        color: var(--white);\n        text-align: center;\n      }\n\n      @media (width > 540px) {\n        .banner__container {\n          grid-template-columns: repeat(2, 1fr);\n        }\n\n        .banner__card:nth-child(1) {\n          grid-area: 1/1/2/3;\n        }\n\n        .order__grid {\n          grid-template-columns: repeat(2, 1fr);\n        }\n      }\n\n      @media (width > 768px) {\n        nav {\n          position: static;\n          padding: 2rem 1rem;\n          display: flex;\n          align-items: center;\n          justify-content: space-between;\n          gap: 1rem;\n        }\n\n        .nav__header {\n          padding: 0;\n          background-color: transparent;\n        }\n\n        .nav__logo img {\n          max-width: 250px;\n        }\n\n        .nav__logo-dark {\n          display: flex;\n        }\n\n        .nav__logo-white {\n          display: none;\n        }\n\n        .nav__menu__btn {\n          display: none;\n        }\n\n        .nav__links {\n          position: static;\n          padding: 0;\n          flex-direction: row;\n          justify-content: flex-end;\n          background-color: transparent;\n          transform: none;\n          z-index: 1;\n        }\n\n        .nav__links a {\n          color: var(--primary-color);\n        }\n\n        .nav__links a:hover {\n          color: var(--tertiary-color);\n        }\n\n        .header__container {\n          grid-template-columns: repeat(2, 1fr);\n          align-items: center;\n        }\n\n        .header__image {\n          grid-area: 1/2/2/3;\n        }\n\n        .header__content h2 {\n          margin-inline-start: unset;\n        }\n\n        .header__content h1 {\n          text-align: left;\n        }\n\n        .banner__card {\n          padding: 1.5rem;\n        }\n\n        .banner__card:nth-child(1) {\n          grid-area: 1/1/3/2;\n        }\n\n        .order__grid {\n          grid-template-columns: repeat(3, 1fr);\n        }\n\n        .event__content {\n          grid-template-columns: repeat(2, 1fr);\n          align-items: center;\n        }\n\n        .event__image {\n          grid-area: 1/2/2/3;\n        }\n\n        .event__details,\n        .event__details .section__header {\n          text-align: left;\n        }\n\n        .reservation__container form {\n          max-width: 600px;\n          grid-template-columns: repeat(2, 1fr);\n        }\n\n        .reservation img {\n          display: flex;\n          position: absolute;\n          z-index: -1;\n        }\n\n        .reservation__bg-1 {\n          left: 0;\n          top: 0;\n          width: clamp(100px, 25vw, 350px);\n        }\n\n        .reservation__bg-2 {\n          right: 0;\n          bottom: 0;\n          width: clamp(100px, 20vw, 250px);\n        }\n\n        .footer__content {\n          grid-template-columns: repeat(2, 1fr);\n        }\n\n        .footer__links li {\n          justify-content: flex-end;\n        }\n\n        .footer__socials {\n          justify-content: flex-end;\n        }\n      }\n\n      @media (width > 1024px) {\n        .order__grid {\n          gap: 2rem;\n        }\n      }\n    </style>\n  </head>\n  <body>\n    <header class=\"header\">\n      <nav>\n        <div class=\"nav__header\">\n          <div class=\"nav__logo\">\n            <a href=\"#\">\n              <img\n                src=\"assets/logo-dark.png\"\n                alt=\"logo\"\n                class=\"nav__logo-dark\"\n              />\n              <img\n                src=\"assets/logo-white.png\"\n                alt=\"logo\"\n                class=\"nav__logo-white\"\n              />\n            </a>\n          </div>\n          <div class=\"nav__menu__btn\" id=\"menu-btn\">\n            <i class=\"ri-menu-line\"></i>\n          </div>\n        </div>\n        <ul class=\"nav__links\" id=\"nav-links\">\n          <li><a href=\"#home\">HOME</a></li>\n          <li><a href=\"#special\">SPECIAL</a></li>\n          <li><a href=\"#menu\">MENU</a></li>\n          <li><a href=\"#event\">EVENTS</a></li>\n          <li><a href=\"#contact\">CONTACT US</a></li>\n        </ul>\n      </nav>\n      <div class=\"section__container header__container\" id=\"home\">\n        <div class=\"header__image\">\n          <img src=\"assets/header.png\" alt=\"header\" />\n        </div>\n        <div class=\"header__content\">\n          <h2>IT IS GOOD TIME FOR THE GREATE TASTE OF BURGER</h2>\n          <h1>BURGER<br /><span>WEEK</span></h1>\n        </div>\n      </div>\n    </header>\n\n    <section class=\"section__container banner__container\" id=\"special\">\n      <div class=\"banner__card\">\n        <p>TRY IT OUT TODAY</p>\n        <h4>MOST POPULAR BURGER</h4>\n      </div>\n      <div class=\"banner__card\">\n        <p>TRY IT OUT TODAY</p>\n        <h4>MORE FUN<br />MORE TASTE</h4>\n      </div>\n      <div class=\"banner__card\">\n        <p>TRY IT OUT TODAY</p>\n        <h4>FRESH & CHILI</h4>\n      </div>\n    </section>\n\n    <section class=\"section__container order__container\" id=\"menu\">\n      <h3>ALWAYS TASTEY BURGER</h3>\n      <h2 class=\"section__header\">CHOOSE & ENJOY</h2>\n      <p class=\"section__description\">\n        Whether you crave classic flavors or daring combinations, this is where\n        your culinary journey begins. Indulge your cravings and savor every bite\n        as you create your personalized burger experience with Burger Company.\n      </p>\n      <div class=\"order__grid\">\n        <div class=\"order__card\">\n          <img src=\"assets/order-1.png\" alt=\"order\" />\n          <h4>Chicken Burger</h4>\n          <p>\n            Sink your teeth into the timeless perfection of our Chicken Burger,\n            an experience that never goes out of style.\n          </p>\n          <button class=\"btn\">ORDER NOW</button>\n        </div>\n        <div class=\"order__card\">\n          <img src=\"assets/order-2.png\" alt=\"order\" />\n          <h4>Veggie Delight Burger</h4>\n          <p>\n            Embrace the vibrant flavors of our Veggie Delight Burger, a\n            celebration of freshness and wholesome goodness.\n          </p>\n          <button class=\"btn\">ORDER NOW</button>\n        </div>\n        <div class=\"order__card\">\n          <img src=\"assets/order-3.png\" alt=\"order\" />\n          <h4>BBQ Bacon Burger</h4>\n          <p>\n            Indulge in a symphony of smoky, savory flavors with our BBQ Bacon\n            Burger, grilled and topped with crispy bacon.\n          </p>\n          <button class=\"btn\">ORDER NOW</button>\n        </div>\n      </div>\n    </section>\n\n    <section class=\"section__container event__container\" id=\"event\">\n      <div class=\"event__content\">\n        <div class=\"event__image\">\n          <img src=\"assets/event.png\" alt=\"event\" />\n        </div>\n        <div class=\"event__details\">\n          <h3>Discover</h3>\n          <h2 class=\"section__header\">UPCOMING EVENTS</h2>\n          <p class=\"section__description\">\n            From exclusive burger tastings and chef collaborations to community\n            outreach initiatives and seasonal celebrations, there's always\n            something special on the horizon at Burger Company. Be the first to\n            know about our upcoming events, promotions, and gatherings as we\n            continue to bring joy and flavor to our cherished customers. Join us\n            in creating memorable moments and delicious memories together!\n          </p>\n        </div>\n      </div>\n    </section>\n\n    <section class=\"reservation\" id=\"contact\">\n      <div class=\"section__container reservation__container\">\n        <h3>RESERVATION</h3>\n        <h2 class=\"section__header\">BOOK YOUR TABLE</h2>\n        <form action=\"/\">\n          <input type=\"text\" placeholder=\"NAME\" />\n          <input type=\"email\" placeholder=\"EMAIL\" />\n          <input type=\"date\" placeholder=\"DATE\" />\n          <input type=\"time\" placeholder=\"TIME\" />\n          <input type=\"number\" placeholder=\"PEOPLE\" />\n          <button class=\"btn\" type=\"submit\">FIND TABLE</button>\n        </form>\n      </div>\n      <img\n        src=\"assets/reservation-bg-1.png\"\n        alt=\"reservation\"\n        class=\"reservation__bg-1\"\n      />\n      <img\n        src=\"assets/reservation-bg-2.png\"\n        alt=\"reservation\"\n        class=\"reservation__bg-2\"\n      />\n    </section>\n\n    <footer class=\"footer\">\n      <div class=\"section__container footer__container\">\n        <div class=\"footer__logo\">\n          <img src=\"assets/logo-white.png\" alt=\"logo\" />\n        </div>\n        <div class=\"footer__content\">\n          <p>\n            Welcome to Burger Company, where passion for exceptional food and\n            genuine hospitality come together. Our story is one of dedication to\n            crafting the perfect burger experience, from sourcing the finest\n            ingredients to delivering unparalleled taste in every bite.\n          </p>\n          <div>\n            <ul class=\"footer__links\">\n              <li>\n                <span><i class=\"ri-map-pin-2-fill\"></i></span>\n                MG Road, Bangalore, 500089\n              </li>\n              <li>\n                <span><i class=\"ri-mail-fill\"></i></span>\n                info@burgerhouse.com\n              </li>\n            </ul>\n            <div class=\"footer__socials\">\n              <a href=\"#\"><i class=\"ri-facebook-circle-fill\"></i></a>\n              <a href=\"#\"><i class=\"ri-instagram-fill\"></i></a>\n              <a href=\"#\"><i class=\"ri-twitter-fill\"></i></a>\n              <a href=\"#\"><i class=\"ri-whatsapp-fill\"></i></a>\n            </div>\n          </div>\n        </div>\n      </div>\n      <div class=\"footer__bar\">\n        Copyright © 2024 Web Design Mastery. All rights reserved.\n      </div>\n    </footer>\n\n    <script src=\"https://unpkg.com/scrollreveal\"></script>\n    <script src=\"main.js\"></script>\n  </body>\n</html>",
      

                                convo.send_message(f"create the HTML part of this project{body} and I have image links that you must use in the wesbite here {image_links}. i have js called script.js and css called style.css files. Make sure the website is professional. use the image links, i gave you. Make the website robust and well detailed. feel free to draw inspiration from this example {inspiration} Generate the website content too. Give no explanations,  just give me the code")
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


                                # import google.generativeai as genai

                                # genai.configure(api_key="AIzaSyD3M4VzknhIcd-ikyA9P4LXiLEoSjH1JQ8")

                                # # Set up the model
                                # generation_config = {
                                # "temperature": 0.9,
                                # "top_p": 1,
                                # "top_k": 1,
                                # "max_output_tokens": 2048,
                                # }

                                # safety_settings = [
                                # {
                                #     "category": "HARM_CATEGORY_HARASSMENT",
                                #     "threshold": "BLOCK_NONE"
                                # },
                                # {
                                #     "category": "HARM_CATEGORY_HATE_SPEECH",
                                #     "threshold": "BLOCK_NONE"
                                # },
                                # {
                                #     "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                                #     "threshold": "BLOCK_NONE"
                                # },
                                # {
                                #     "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                                #     "threshold": "BLOCK_NONE"
                                # },
                                # ]

                                # model = genai.GenerativeModel(model_name="gemini-1.5-flash-002",
                                #                             generation_config=generation_config,
                                #                             safety_settings=safety_settings)

                                # convo = model.start_chat(history=[
                                # ])

                                # inspiration = "<!DOCTYPE html>\n<html lang=\"en\">\n  <head>\n    <meta charset=\"UTF-8\" />\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />\n    <link\n      href=\"https://cdn.jsdelivr.net/npm/remixicon@4.2.0/fonts/remixicon.css\"\n      rel=\"stylesheet\"\n    />\n    <title>Web Design Mastery | Burger House</title>\n    <style>\n      @import url(\"https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Bebas+Neue&family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap\");\n\n      :root {\n        --primary-color: #42200b;\n        --secondary-color: #ffc135;\n        --tertiary-color: #df1c1c;\n        --text-dark: #212529;\n        --white: #ffffff;\n        --max-width: 1200px;\n        --header-font-1: \"Alfa Slab One\", serif;\n        --header-font-2: \"Bebas Neue\", sans-serif;\n      }\n\n      * {\n        padding: 0;\n        margin: 0;\n        box-sizing: border-box;\n      }\n\n      .section__container {\n        max-width: var(--max-width);\n        margin: auto;\n        padding: 5rem 1rem;\n      }\n\n      .section__header {\n        font-size: 3rem;\n        font-weight: 500;\n        font-family: var(--header-font-1);\n        color: var(--primary-color);\n        text-align: center;\n        line-height: 3.75rem;\n        text-shadow: 2px 2px var(--secondary-color);\n      }\n\n      .section__description {\n        font-weight: 500;\n        color: var(--text-dark);\n        line-height: 1.75rem;\n      }\n\n      .btn {\n        padding: 1rem 1.5rem;\n        outline: none;\n        border: none;\n        font-size: 1rem;\n        color: var(--white);\n        background-color: var(--tertiary-color);\n        transition: 0.3s;\n        cursor: pointer;\n      }\n\n      .btn:hover {\n        background-color: var(--primary-color);\n      }\n\n      img {\n        display: flex;\n        width: 100%;\n      }\n\n      a {\n        text-decoration: none;\n        transition: 0.3s;\n      }\n\n      html,\n      body {\n        scroll-behavior: smooth;\n      }\n\n      body {\n        font-family: \"Montserrat\", sans-serif;\n      }\n\n      .header {\n        background-image: url(\"assets/header-bg.png\");\n        background-position: center center;\n        background-size: cover;\n        background-repeat: no-repeat;\n      }\n\n      nav {\n        position: fixed;\n        width: 100%;\n        max-width: var(--max-width);\n        margin-inline: auto;\n        z-index: 9;\n      }\n\n      .nav__header {\n        padding: 1rem;\n        display: flex;\n        align-items: center;\n        justify-content: space-between;\n        background-color: var(--primary-color);\n      }\n\n      .nav__logo img {\n        max-width: 150px;\n      }\n\n      .nav__logo-dark {\n        display: none;\n      }\n\n      .nav__menu__btn {\n        font-size: 1.5rem;\n        color: var(--white);\n        cursor: pointer;\n      }\n\n      .nav__links {\n        position: absolute;\n        top: 60px;\n        left: 0;\n        width: 100%;\n        padding: 2rem;\n        list-style: none;\n        display: flex;\n        align-items: center;\n        justify-content: center;\n        flex-direction: column;\n        gap: 2rem;\n        background-color: var(--primary-color);\n        transition: 0.5s;\n        z-index: -1;\n        transform: translateY(-100%);\n      }\n\n      .nav__links.open {\n        transform: translateY(0);\n      }\n\n      .nav__links a {\n        font-weight: 600;\n        white-space: nowrap;\n        color: var(--white);\n        transition: 0.3s;\n      }\n\n      .nav__links a:hover {\n        color: var(--secondary-color);\n      }\n\n      .header__container {\n        display: grid;\n        gap: 2rem;\n        overflow: hidden;\n      }\n\n      .header__image img {\n        max-width: 600px;\n        margin-inline: auto;\n      }\n\n      .header__content h2 {\n        max-width: 400px;\n        margin-inline: auto;\n        margin-bottom: 2rem;\n        padding: 1rem 2rem;\n        font-size: 1.75rem;\n        font-weight: 400;\n        font-family: var(--header-font-2);\n        color: var(--primary-color);\n        border: 2px dashed var(--primary-color);\n        text-align: center;\n      }\n\n      .header__content h1 {\n        font-size: 4.5rem;\n        font-weight: 500;\n        font-family: var(--header-font-1);\n        color: var(--primary-color);\n        line-height: 3.5rem;\n        text-align: center;\n        text-shadow: 2px 2px var(--white);\n      }\n\n      .header__content h1 span {\n        font-size: 3rem;\n      }\n\n      .banner__container {\n        display: grid;\n        gap: 1rem;\n        grid-auto-rows: 200px;\n      }\n\n      .banner__card {\n        padding: 1rem;\n        background-position: center center;\n        background-size: cover;\n        background-repeat: no-repeat;\n        border-radius: 1rem;\n      }\n\n      .banner__card:nth-child(1) {\n        background-image: url(\"assets/banner-1.png\");\n      }\n\n      .banner__card:nth-child(2) {\n        background-image: url(\"assets/banner-2.png\");\n      }\n\n      .banner__card:nth-child(3) {\n        background-image: url(\"assets/banner-3.png\");\n      }\n\n      .banner__card p {\n        margin-bottom: 0.5rem;\n        font-size: 1.5rem;\n        font-weight: 500;\n        color: var(--white);\n      }\n\n      .banner__card h4 {\n        font-size: 2rem;\n        font-weight: 600;\n        color: var(--white);\n      }\n\n      .order__container h3 {\n        max-width: fit-content;\n        margin-inline: auto;\n        margin-bottom: 1rem;\n        padding: 0.5rem 2rem;\n        font-size: 1.5rem;\n        font-weight: 400;\n        font-family: var(--header-font-2);\n        color: var(--primary-color);\n        background-color: var(--secondary-color);\n      }\n\n      .order__container .section__header {\n        margin-bottom: 1rem;\n      }\n\n      .order__container .section__description {\n        margin-bottom: 2rem;\n        text-align: center;\n      }\n\n      .order__grid {\n        display: grid;\n        gap: 2rem 1rem;\n      }\n\n      .order__card {\n        padding: 2rem 1rem;\n        border-radius: 1rem;\n        text-align: center;\n        transition: 0.3s;\n      }\n\n      .order__card:hover {\n        box-shadow: 5px 5px 30px rgba(0, 0, 0, 0.1);\n      }\n\n      .order__card img {\n        max-width: 250px;\n        margin-inline: auto;\n        margin-bottom: 2rem;\n        filter: drop-shadow(10px 10px 30px rgba(0, 0, 0, 0.3));\n      }\n\n      .order__card h4 {\n        margin-bottom: 1rem;\n        font-size: 1.5rem;\n        font-weight: 600;\n        color: var(--text-dark);\n      }\n\n      .order__card p {\n        margin-bottom: 2rem;\n        font-weight: 500;\n        color: var(--text-dark);\n        line-height: 1.75rem;\n      }\n\n      .event__content {\n        display: grid;\n        gap: 2rem;\n        padding: 1rem;\n        box-shadow: 5px 5px 20px rgba(0, 0, 0, 0.1);\n      }\n\n      .event__details {\n        text-align: center;\n      }\n\n      .event__details h3 {\n        font-size: 2rem;\n        font-weight: 500;\n        font-family: var(--header-font-2);\n        color: var(--text-dark);\n      }\n\n      .event__details .section__header {\n        margin-bottom: 1rem;\n      }\n\n      .reservation {\n        position: relative;\n        isolation: isolate;\n      }\n\n      .reservation__container h3 {\n        font-size: 2rem;\n        font-weight: 500;\n        font-family: var(--header-font-2);\n        color: var(--text-dark);\n        text-align: center;\n      }\n\n      .reservation__container form {\n        max-width: 400px;\n        margin-inline: auto;\n        margin-top: 4rem;\n        display: grid;\n        gap: 1rem;\n      }\n\n      .reservation__container input {\n        padding: 0.75rem 1rem;\n        outline: none;\n        border: 1px solid var(--text-dark);\n        font-size: 1rem;\n        color: var(--text-dark);\n      }\n\n      .reservation__container input::placeholder {\n        color: var(--text-dark);\n      }\n\n      .reservation img {\n        display: none;\n      }\n\n      .footer {\n        background-image: url(\"assets/footer-bg.png\");\n        background-position: center center;\n        background-size: cover;\n        background-repeat: no-repeat;\n      }\n\n      .footer__logo img {\n        max-width: 250px;\n      }\n\n      .footer__content {\n        margin-top: 2rem;\n        display: grid;\n        gap: 2rem;\n      }\n\n      .footer__content p {\n        font-weight: 5500;\n        color: var(--white);\n        line-height: 1.75rem;\n      }\n\n      .footer__links {\n        list-style: none;\n        display: grid;\n        gap: 1rem;\n      }\n\n      .footer__links li {\n        display: flex;\n        align-items: center;\n        gap: 1rem;\n        font-weight: 500;\n        color: var(--white);\n      }\n\n      .footer__links li span {\n        font-size: 1.25rem;\n      }\n\n      .footer__socials {\n        margin-top: 2rem;\n        display: flex;\n        align-items: center;\n        gap: 1rem;\n      }\n\n      .footer__socials a {\n        font-size: 1.5rem;\n        color: var(--white);\n      }\n\n      .footer__socials a:hover {\n        color: var(--secondary-color);\n      }\n\n      .footer__bar {\n        padding: 1rem;\n        font-size: 0.9rem;\n        color: var(--white);\n        text-align: center;\n      }\n\n      @media (width > 540px) {\n        .banner__container {\n          grid-template-columns: repeat(2, 1fr);\n        }\n\n        .banner__card:nth-child(1) {\n          grid-area: 1/1/2/3;\n        }\n\n        .order__grid {\n          grid-template-columns: repeat(2, 1fr);\n        }\n      }\n\n      @media (width > 768px) {\n        nav {\n          position: static;\n          padding: 2rem 1rem;\n          display: flex;\n          align-items: center;\n          justify-content: space-between;\n          gap: 1rem;\n        }\n\n        .nav__header {\n          padding: 0;\n          background-color: transparent;\n        }\n\n        .nav__logo img {\n          max-width: 250px;\n        }\n\n        .nav__logo-dark {\n          display: flex;\n        }\n\n        .nav__logo-white {\n          display: none;\n        }\n\n        .nav__menu__btn {\n          display: none;\n        }\n\n        .nav__links {\n          position: static;\n          padding: 0;\n          flex-direction: row;\n          justify-content: flex-end;\n          background-color: transparent;\n          transform: none;\n          z-index: 1;\n        }\n\n        .nav__links a {\n          color: var(--primary-color);\n        }\n\n        .nav__links a:hover {\n          color: var(--tertiary-color);\n        }\n\n        .header__container {\n          grid-template-columns: repeat(2, 1fr);\n          align-items: center;\n        }\n\n        .header__image {\n          grid-area: 1/2/2/3;\n        }\n\n        .header__content h2 {\n          margin-inline-start: unset;\n        }\n\n        .header__content h1 {\n          text-align: left;\n        }\n\n        .banner__card {\n          padding: 1.5rem;\n        }\n\n        .banner__card:nth-child(1) {\n          grid-area: 1/1/3/2;\n        }\n\n        .order__grid {\n          grid-template-columns: repeat(3, 1fr);\n        }\n\n        .event__content {\n          grid-template-columns: repeat(2, 1fr);\n          align-items: center;\n        }\n\n        .event__image {\n          grid-area: 1/2/2/3;\n        }\n\n        .event__details,\n        .event__details .section__header {\n          text-align: left;\n        }\n\n        .reservation__container form {\n          max-width: 600px;\n          grid-template-columns: repeat(2, 1fr);\n        }\n\n        .reservation img {\n          display: flex;\n          position: absolute;\n          z-index: -1;\n        }\n\n        .reservation__bg-1 {\n          left: 0;\n          top: 0;\n          width: clamp(100px, 25vw, 350px);\n        }\n\n        .reservation__bg-2 {\n          right: 0;\n          bottom: 0;\n          width: clamp(100px, 20vw, 250px);\n        }\n\n        .footer__content {\n          grid-template-columns: repeat(2, 1fr);\n        }\n\n        .footer__links li {\n          justify-content: flex-end;\n        }\n\n        .footer__socials {\n          justify-content: flex-end;\n        }\n      }\n\n      @media (width > 1024px) {\n        .order__grid {\n          gap: 2rem;\n        }\n      }\n    </style>\n  </head>\n  <body>\n    <header class=\"header\">\n      <nav>\n        <div class=\"nav__header\">\n          <div class=\"nav__logo\">\n            <a href=\"#\">\n              <img\n                src=\"assets/logo-dark.png\"\n                alt=\"logo\"\n                class=\"nav__logo-dark\"\n              />\n              <img\n                src=\"assets/logo-white.png\"\n                alt=\"logo\"\n                class=\"nav__logo-white\"\n              />\n            </a>\n          </div>\n          <div class=\"nav__menu__btn\" id=\"menu-btn\">\n            <i class=\"ri-menu-line\"></i>\n          </div>\n        </div>\n        <ul class=\"nav__links\" id=\"nav-links\">\n          <li><a href=\"#home\">HOME</a></li>\n          <li><a href=\"#special\">SPECIAL</a></li>\n          <li><a href=\"#menu\">MENU</a></li>\n          <li><a href=\"#event\">EVENTS</a></li>\n          <li><a href=\"#contact\">CONTACT US</a></li>\n        </ul>\n      </nav>\n      <div class=\"section__container header__container\" id=\"home\">\n        <div class=\"header__image\">\n          <img src=\"assets/header.png\" alt=\"header\" />\n        </div>\n        <div class=\"header__content\">\n          <h2>IT IS GOOD TIME FOR THE GREATE TASTE OF BURGER</h2>\n          <h1>BURGER<br /><span>WEEK</span></h1>\n        </div>\n      </div>\n    </header>\n\n    <section class=\"section__container banner__container\" id=\"special\">\n      <div class=\"banner__card\">\n        <p>TRY IT OUT TODAY</p>\n        <h4>MOST POPULAR BURGER</h4>\n      </div>\n      <div class=\"banner__card\">\n        <p>TRY IT OUT TODAY</p>\n        <h4>MORE FUN<br />MORE TASTE</h4>\n      </div>\n      <div class=\"banner__card\">\n        <p>TRY IT OUT TODAY</p>\n        <h4>FRESH & CHILI</h4>\n      </div>\n    </section>\n\n    <section class=\"section__container order__container\" id=\"menu\">\n      <h3>ALWAYS TASTEY BURGER</h3>\n      <h2 class=\"section__header\">CHOOSE & ENJOY</h2>\n      <p class=\"section__description\">\n        Whether you crave classic flavors or daring combinations, this is where\n        your culinary journey begins. Indulge your cravings and savor every bite\n        as you create your personalized burger experience with Burger Company.\n      </p>\n      <div class=\"order__grid\">\n        <div class=\"order__card\">\n          <img src=\"assets/order-1.png\" alt=\"order\" />\n          <h4>Chicken Burger</h4>\n          <p>\n            Sink your teeth into the timeless perfection of our Chicken Burger,\n            an experience that never goes out of style.\n          </p>\n          <button class=\"btn\">ORDER NOW</button>\n        </div>\n        <div class=\"order__card\">\n          <img src=\"assets/order-2.png\" alt=\"order\" />\n          <h4>Veggie Delight Burger</h4>\n          <p>\n            Embrace the vibrant flavors of our Veggie Delight Burger, a\n            celebration of freshness and wholesome goodness.\n          </p>\n          <button class=\"btn\">ORDER NOW</button>\n        </div>\n        <div class=\"order__card\">\n          <img src=\"assets/order-3.png\" alt=\"order\" />\n          <h4>BBQ Bacon Burger</h4>\n          <p>\n            Indulge in a symphony of smoky, savory flavors with our BBQ Bacon\n            Burger, grilled and topped with crispy bacon.\n          </p>\n          <button class=\"btn\">ORDER NOW</button>\n        </div>\n      </div>\n    </section>\n\n    <section class=\"section__container event__container\" id=\"event\">\n      <div class=\"event__content\">\n        <div class=\"event__image\">\n          <img src=\"assets/event.png\" alt=\"event\" />\n        </div>\n        <div class=\"event__details\">\n          <h3>Discover</h3>\n          <h2 class=\"section__header\">UPCOMING EVENTS</h2>\n          <p class=\"section__description\">\n            From exclusive burger tastings and chef collaborations to community\n            outreach initiatives and seasonal celebrations, there's always\n            something special on the horizon at Burger Company. Be the first to\n            know about our upcoming events, promotions, and gatherings as we\n            continue to bring joy and flavor to our cherished customers. Join us\n            in creating memorable moments and delicious memories together!\n          </p>\n        </div>\n      </div>\n    </section>\n\n    <section class=\"reservation\" id=\"contact\">\n      <div class=\"section__container reservation__container\">\n        <h3>RESERVATION</h3>\n        <h2 class=\"section__header\">BOOK YOUR TABLE</h2>\n        <form action=\"/\">\n          <input type=\"text\" placeholder=\"NAME\" />\n          <input type=\"email\" placeholder=\"EMAIL\" />\n          <input type=\"date\" placeholder=\"DATE\" />\n          <input type=\"time\" placeholder=\"TIME\" />\n          <input type=\"number\" placeholder=\"PEOPLE\" />\n          <button class=\"btn\" type=\"submit\">FIND TABLE</button>\n        </form>\n      </div>\n      <img\n        src=\"assets/reservation-bg-1.png\"\n        alt=\"reservation\"\n        class=\"reservation__bg-1\"\n      />\n      <img\n        src=\"assets/reservation-bg-2.png\"\n        alt=\"reservation\"\n        class=\"reservation__bg-2\"\n      />\n    </section>\n\n    <footer class=\"footer\">\n      <div class=\"section__container footer__container\">\n        <div class=\"footer__logo\">\n          <img src=\"assets/logo-white.png\" alt=\"logo\" />\n        </div>\n        <div class=\"footer__content\">\n          <p>\n            Welcome to Burger Company, where passion for exceptional food and\n            genuine hospitality come together. Our story is one of dedication to\n            crafting the perfect burger experience, from sourcing the finest\n            ingredients to delivering unparalleled taste in every bite.\n          </p>\n          <div>\n            <ul class=\"footer__links\">\n              <li>\n                <span><i class=\"ri-map-pin-2-fill\"></i></span>\n                MG Road, Bangalore, 500089\n              </li>\n              <li>\n                <span><i class=\"ri-mail-fill\"></i></span>\n                info@burgerhouse.com\n              </li>\n            </ul>\n            <div class=\"footer__socials\">\n              <a href=\"#\"><i class=\"ri-facebook-circle-fill\"></i></a>\n              <a href=\"#\"><i class=\"ri-instagram-fill\"></i></a>\n              <a href=\"#\"><i class=\"ri-twitter-fill\"></i></a>\n              <a href=\"#\"><i class=\"ri-whatsapp-fill\"></i></a>\n            </div>\n          </div>\n        </div>\n      </div>\n      <div class=\"footer__bar\">\n        Copyright © 2024 Web Design Mastery. All rights reserved.\n      </div>\n    </footer>\n\n    <script src=\"https://unpkg.com/scrollreveal\"></script>\n    <script src=\"main.js\"></script>\n  </body>\n</html>",
      

                                # convo.send_message(f"generating code only, create the CSS PART of this project{body}, considering this is the html part {html_output} feel free to be creative, follow the implmentation of css here {inspiration}, learn from it, make sure the website is well designed and the displays professioanlism. Give no explanations, just pure code. Make it look good, please and have an hero segment")
                                # convo.send_message(f"generating code only, create the CSS PART of this project{body}, considering this is the html part {html_output} feel free to be creative, follow the implmentation of css here {inspiration}, learn from it, make sure the website is well designed and the displays professioanlism. Give no explanations, just pure code. Make it look good, please and have an hero segment")
                               
                                # css_content = convo.last.text
                                # css_output = css_content
                                # print(css_content)



                                
                                from importlib.metadata import version
                                from packaging.version import parse
                                import anthropic

                                anthropic_version = parse(version("anthropic"))

                                client = anthropic.Anthropic(
                                    # defaults to os.environ.get("ANTHROPIC_API_KEY")
                                    api_key="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",
                                )
                                message = client.messages.create(
                                    model="claude-3-5-sonnet-20240620",
                                    max_tokens=3096,
                                    temperature=0,
                                    system="Your are the ultimate css coder. You are the best website builder designer ever. you give back code only. ",
                                    messages=[
                                        {
                                            "role": "user",
                                            "content": [
                                                {
                                                    "type": "text",
                                                    "text": f"genating code only, create the CSS PART of this project{body}, considering this is the html part {html_output}. Make the styling extensive and sphisticated. Complete the css design and styling. The design should be robust detailed and good. Ensure that the color theme matches the entire project, Make sure that the images all are well sized and not too large at any point. make it look very good and professioany made. Make it well aligned and use creative fonts that match the theme. Make sure the website is perfect and clean. generate code only no explanations. Make the styling part look good please, dont make it too plain"}
                                            ]
                                        }
                                    ]
                                )
                                css_output = message.content
                                css_content = css_output[0].text
                                css_output = css_content





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



                                convo.send_message(f"genating code only, create the JS PART of this project{body}, considering this is the html part {html_output} feel free to be creative, make sure the website is well designed and the displays professioanlism. follow the js implementation here {inspiration}Give no explanations, just pure code")
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
                                os.makedirs("website_bot", exist_ok=True)

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
                                chat_history  = []

                                

            
                    # No else case, just ignore if the text/body isn't present
    except (KeyError, IndexError) as e:
        pass  # Just ignore and do nothing
    
    return "OK", 200 




if __name__ == "__main__":
    print(f"Starting server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=True)










