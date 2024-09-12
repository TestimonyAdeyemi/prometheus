

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