import requests
import os

# Define the URL of the file
url = "https://greenteapress.com/thinkpython2/code/words.txt"

# Define the local path where the file should be saved
local_path = os.path.expanduser("~/Desktop/words.txt")

# Check if the directory exists, if not create it
directory = os.path.dirname(local_path)
if not os.path.exists(directory):
    os.makedirs(directory)

try:
    # Attempt to download the file
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the request failed

    # Save the file to the local path
    with open(local_path, "wb") as file:
        file.write(response.content)

    # Calculate the number of words in the file
    with open(local_path, "r") as file:
        words = file.read().split()
        word_count = len(words)

    print(
        f"File successfully downloaded and saved to {local_path}. Number of words: {word_count}"
    )

except requests.exceptions.RequestException as e:
    # Handle any errors that occurred during the request
    print(f"An error occurred while trying to download the file: {e}")

except Exception as e:
    # Handle other exceptions
    print(f"An unexpected error occurred: {e}")
