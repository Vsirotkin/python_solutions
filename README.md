# PYTHON-SOLUTIONS

================================================================================
1. # Text Encryption and Decryption Script

## Overview

This script performs a series of operations on a given sentence to encrypt and subsequently decrypt it. The process involves cleaning the sentence, downloading and shuffling a dictionary file, inserting new words into the dictionary if necessary, collecting words based on user input, and finally reversing the words for encryption. The decryption process reverses the encryption steps to retrieve the original sentence.

## Features

- **Sentence Cleaning**: Removes punctuation and converts the sentence to lowercase.
- **Dictionary Management**: Downloads a dictionary file if it doesn't exist, shuffles its contents, and ensures all words from the sentence are included.
- **Word Collection**: Collects words from the shuffled dictionary based on user-defined parameters for start point, number of words to collect, and step size.
- **Encryption**: Inserts collected words into the spaces of the cleaned sentence, reverses each word, and converts them to lowercase.
- **Decryption**: Reverses the encryption by reversing each word back to its original form and removing any words that were not originally in the dictionary.

## Requirements

- Python 3.6 or higher
- `requests` library

## Installation

1. Clone the repository or download the script.
2. Install the required Python package:
   ```sh
   pip install requests
   ```

## Usage

1. Run the script:
   ```sh
   python script_name.py
   ```
2. Enter the required inputs when prompted:
   - Start point: The index from which to start collecting words.
   - How many words to collect for each space: The number of words to insert between each original word.
   - Step: The number of words to skip after each collection.


## Notes

- Ensure that the URL for the dictionary file is accessible and does not require authentication.
- The script handles basic text processing and assumes that the dictionary file is a plain text file with one word per line.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Disclaimer

This script is intended for educational purposes only. Use it responsibly and ensure compliance with the terms of service of the websites you are accessing.

================================================================================
2. # Webpage Word Counter Script

## Overview

This script is designed to count the number of words on a specified webpage. It uses the `requests` library to fetch the webpage content and `BeautifulSoup` from the `bs4` library to parse the HTML and extract the text. The script then splits the text into individual words and counts them.

## Features

- **Webpage Fetching**: Uses the `requests` library to fetch the content of a specified webpage.
- **HTML Parsing**: Utilizes `BeautifulSoup` to parse the HTML and extract the text content.
- **Word Counting**: Splits the extracted text into words and counts them.
- **Error Handling**: Checks if the webpage was successfully retrieved and handles cases where the request fails.

## Requirements

- Python 3.6 or higher
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone the repository or download the script.
2. Install the required Python packages:
   ```sh
   pip install requests beautifulsoup4
   ```

## Usage

1. Open the script file and set the `url` variable to the webpage you want to analyze.
2. Run the script:
   ```sh
   python count_words.py
   ```
3. The script will output the number of words found on the webpage.


## Notes

- Ensure that the URL provided is accessible and does not require authentication.
- The script counts all words, including those in scripts and stylesheets if not properly filtered out by `BeautifulSoup`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Disclaimer

This script is intended for educational purposes only. Use it responsibly and ensure compliance with the terms of service of the websites you are accessing.

================================================================================
3. # WhatsApp Message Sender Script

## Overview

This script is designed to send promotional messages to multiple phone numbers using WhatsApp Web. It reads phone numbers and corresponding names from a file named `phones.txt`, constructs personalized messages, and sends them sequentially to avoid being flagged as spam. The script ensures that only one browser tab is open at a time by closing the previous session before opening a new one.

## Features

- **Sequential Message Sending**: Ensures that messages are sent one at a time to avoid being flagged as spam.
- **Session Management**: Closes the previous browser session before opening a new one to maintain a single active tab.
- **Personalized Messages**: Constructs messages with personalized greetings based on the names provided in the input file.
- **Error Handling**: Provides error handling to catch and report issues encountered during message sending.
- **Completion Notification**: Informs the user when all messages have been successfully sent.

## Requirements

- Python 3.7 or higher
- `pyautogui` library
- `psutil` library
- `tkinter` library (for `pyautogui`'s `MouseInfo` functionality)

## Installation

1. Clone the repository or download the script.
2. Install the required Python packages:
   ```sh
   pip install pyautogui psutil
   ```
3. Ensure `tkinter` is installed on your system. On Linux, you can install it using:
   ```sh
   sudo apt-get install python3-tk
   ```

## Usage

1. Create a file named `phones.txt` in the same directory as the script. Each line should contain a phone number and a name separated by a comma, e.g.:
   ```
   1234567890, John Doe
   0987654321, Jane Smith
   ```
2. Run the script:
   ```sh
   python whatsapp_message_sender.py
   ```
3. The script will open WhatsApp Web in your default browser, send the messages sequentially, and close the browser after each message.

## Notes

- Ensure that you have WhatsApp Web logged in on your browser before running the script.
- The script uses `pyautogui` to interact with the browser, so make sure that the browser window is in focus and not minimized.
- The script waits for 8 (user's adjustable) seconds for the WhatsApp Web page to load before sending each message. Adjust this time if necessary.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Disclaimer

This script is intended for educational purposes only. Use it responsibly and ensure compliance with WhatsApp's terms of service.


================================================================================
4. # XKCD Comic Downloader

## Overview

This Python script, `downloadXkcd.py`, automates the process of downloading the first 10 XKCD comics from the web. It uses the `requests` library to fetch web pages and images, and `BeautifulSoup` from the `bs4` library to parse HTML and find the comic images.

## Features

- **Automated Downloading**: The script automatically navigates through the XKCD archive to download the first 10 comics.
- **Error Handling**: Utilizes `requests.raise_for_status()` to ensure that any issues with downloading are immediately reported.
- **Directory Management**: Creates a directory named `xkcd` to store the downloaded comic images.

## Requirements

- Python 3.x
- `requests` library
- `bs4` (BeautifulSoup) library

## Installation

1. Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Install the required libraries using pip:
   ```bash
   pip install requests beautifulsoup4
   ```

## Usage

1. Save the script to a file named `downloadXkcd.py`.
2. Run the script from the command line:
   ```bash
   python downloadXkcd.py
   ```
3. The script will create a directory named `xkcd` in the same directory as the script and save the downloaded comics there.

## How It Works

- The script starts at the XKCD homepage and navigates backward through the comics using the "Prev" button.
- For each page, it locates the comic image using HTML selectors and downloads the image.
- The process continues until 10 comics have been downloaded or the beginning of the archive is reached.

## Notes

- The script assumes that the structure of the XKCD website remains consistent with the selectors used.
- If the website structure changes, the script may need to be updated to reflect these changes.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or bug fixes.
