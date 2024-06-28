""" go online and count the number of words on the webpage """

import requests
from bs4 import BeautifulSoup

# URL of the webpage
url = "https://inventwithpython.com/dictionary.txt"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content of the response using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract the text from the webpage
    text = soup.get_text()

    # Split the text into words
    words = text.split()

    # Count the number of words
    word_count = len(words)

    print(f"The number of words on the webpage is: {word_count}")
else:
    print("Failed to retrieve the webpage")
