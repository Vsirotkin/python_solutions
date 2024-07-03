# Automated WhatsApp Messaging

This project provides two different approaches to automate sending messages via WhatsApp Web: one using `pyautogui` for GUI automation and another using `selenium` with CSS selectors for web automation.

## Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Options](#options)
   - [Option 1: Using `pyautogui`](#option-1-using-pyautogui)
   - [Option 2: Using `selenium` with CSS Selector](#option-2-using-selenium-with-css-selector)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

Automating WhatsApp messages can be useful for various purposes such as sending notifications, reminders, or updates to a list of contacts. This project offers two methods to achieve this automation:

- **Option 1**: Uses `pyautogui` to control the mouse and keyboard, suitable for simple GUI interactions.
- **Option 2**: Uses `selenium` for web automation, providing more robust and scalable solutions for web-based interactions.

## Prerequisites

- Python 3.6 or higher
- `pyautogui` library (for Option 1)
- `selenium` library (for Option 2)
- `geckodriver` (for Option 2, if using Firefox)
- A file named `phones.txt` containing phone numbers and names in the format: `phone_number,name`

## Setup

1. **Install Python**: Ensure Python is installed on your system.
2. **Install Required Libraries**:
   - For Option 1:
     ```bash
     pip install pyautogui
     ```
   - For Option 2:
     ```bash
     pip install selenium
     ```
3. **Download `geckodriver`**:
   - For Option 2, download `geckodriver` from [here](https://github.com/mozilla/geckodriver/releases) and place it in a directory included in your system's PATH.

## Usage

1. **Prepare `phones.txt`**:
   - Create a file named `phones.txt` in the project directory.
   - Populate it with phone numbers and names in the format:
     ```
     +1234567890,John Doe
     +0987654321,Jane Smith
     ```

2. **Run the Script**:
   - For Option 1:
     ```bash
     python script_pyautogui.py
     ```
   - For Option 2:
     ```bash
     python script_selenium.py
     ```

## Options

### Option 1: Using `pyautogui`

- **Description**: This script uses `pyautogui` to automate the process of opening WhatsApp Web, navigating to the chat, and sending a message.
- **Limitations**:
  - Relies on GUI interactions, which can be less reliable.
  - Requires the browser window to be in focus and properly sized.

### Option 2: Using `selenium` with CSS Selector

- **Description**: This script uses `selenium` to automate the process of opening WhatsApp Web, navigating to the chat, and sending a message using CSS selectors for precise element targeting.
- **Advantages**:
  - More robust and scalable for web-based automation.
  - Handles dynamic web elements more effectively.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
