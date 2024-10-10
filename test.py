# import requests

#  # Send response back to WhatsApp
# url = "https://graph.facebook.com/v20.0/396015606935687/messages"
# headers = {
#     "Authorization": "Bearer EAAPPDu1MMoEBOzXqZCfroxXGYyono1AvwrkrTrg8OyhlH0KjTzqr9F5W36lvyZCV3fDoxpp92AgGnyKyRbt8ihOJ0za2PnsRJK3ZAhW4ZBoyeZBmzWKWAn9BZCouOQ9gghESIUG6xNxJlUJRlu6KwiQNHu7v3doZCCeKg8lN4qiPfCYZCcC0N5WVMmUqd2DYXir7EwZDZD",
#     "Content-Type": "application/json"
# }
# wa_id = "2348143237903"
# output = "testing.."
# data = {
#     "messaging_product": "whatsapp",
#     "to": wa_id,
#     "type": "text",
#     "text": {
#         "body": output
#     }
# }

# response = requests.post(url, headers=headers, json=data)


# import requests
# import os
# # Netlify API endpoint
# NETLIFY_API = "https://api.netlify.com/api/v1"

# def deploy_to_netlify(access_token, directory_path, site_name=None):
#     # Validate the directory
#     if not os.path.isdir(directory_path):
#         raise ValueError(f"The specified path '{directory_path}' is not a valid directory.")

#     # Prepare the headers for the API request
#     headers = {
#         "Authorization": f"Bearer {access_token}",
#         "Content-Type": "application/zip"
#     }

#     # Zip the directory
#     zip_path = "site.zip"
#     os.system(f"zip -r {zip_path} {directory_path}")

#     # Create a new site if site_name is provided
#     if site_name:
#         import requests
#         create_site_response = requests.post(
#             f"{NETLIFY_API}/sites",
#             headers=headers,
#             json={"name": site_name}
#         )
#         if create_site_response.status_code != 201:
#             print(f"Failed to create site. Status code: {create_site_response.status_code}")
#             print(f"Error message: {create_site_response.text}")
#             return
#         site_id = create_site_response.json()["id"]
#         print(f"Created new site with ID: {site_id}")
#     else:
#         # If no site_name is provided, deploy to the user's first site
#         sites_response = requests.get(f"{NETLIFY_API}/sites", headers=headers)
#         if sites_response.status_code != 200 or not sites_response.json():
#             print("No existing sites found and no site name provided to create a new one.")
#             return
#         site_id = sites_response.json()[0]["id"]
#         print(f"Deploying to existing site with ID: {site_id}")

#     # Upload the zipped site
#     with open(zip_path, "rb") as zip_file:
#         response = requests.post(
#             f"{NETLIFY_API}/sites/{site_id}/deploys",
#             headers=headers,
#             data=zip_file
#         )

#     # Clean up the zip file
#     os.remove(zip_path)

#     # Check the response
#     if response.status_code == 200:
#         deploy_url = response.json()["deploy_url"]
#         print(f"Deployment successful! Your site is live at: {deploy_url}")

        
#     else:
#         print(f"Deployment failed. Status code: {response.status_code}")
#         print(f"Error message: {response.text}")

# # Usage
# access_token = "nfp_4uUmEKzfAsAa1dmVYedSeebLDEw6DKmT49a8"
# directory_path = "ai"
# site_name = "my-awesome-site"  # Optional: Provide a name to create a new site



# deploy_to_netlify(access_token, directory_path, site_name)







# from huggingface_hub import InferenceClient

# client = InferenceClient(api_key="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")

# for message in client.chat_completion(
# 	model="meta-llama/Llama-3.1-8B-Instruct",
# 	messages=[{"role": "user", "content": "What is the capital of France?"}],
# 	max_tokens=500,
# 	stream=True,
# ):
#     print(message.choices[0].delta.content, end="")




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
search_query = "african hairstyles pinterest"
image_urls = get_image_urls(search_query)

# Display the image URLs
print("Image URLs:", image_urls)

image_links = image_urls