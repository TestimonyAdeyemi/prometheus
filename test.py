import requests

 # Send response back to WhatsApp
url = "https://graph.facebook.com/v20.0/396015606935687/messages"
headers = {
    "Authorization": "Bearer EAAPPDu1MMoEBOzXqZCfroxXGYyono1AvwrkrTrg8OyhlH0KjTzqr9F5W36lvyZCV3fDoxpp92AgGnyKyRbt8ihOJ0za2PnsRJK3ZAhW4ZBoyeZBmzWKWAn9BZCouOQ9gghESIUG6xNxJlUJRlu6KwiQNHu7v3doZCCeKg8lN4qiPfCYZCcC0N5WVMmUqd2DYXir7EwZDZD",
    "Content-Type": "application/json"
}
wa_id = "2348143237903"
output = "testing.."
data = {
    "messaging_product": "whatsapp",
    "to": wa_id,
    "type": "text",
    "text": {
        "body": output
    }
}

response = requests.post(url, headers=headers, json=data)


