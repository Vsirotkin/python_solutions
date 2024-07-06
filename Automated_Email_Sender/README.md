 ## Automated Email Sender

This script allows you to send automated emails using a Gmail account. It uses environment variables to securely store your Gmail credentials and can be run from the command line with the recipient's email address and the message as arguments.

## Features

- Securely stores Gmail credentials using environment variables.
- Sends both plain text and HTML versions of the email.
- Easy to use from the command line.

## Requirements

- Python 3.6 or higher
- A Gmail account with "Less secure app access" enabled (for development purposes only; consider using OAuth2 for production).
- `python-dotenv` package

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/automated-email-sender.git
   cd automated-email-sender
   ```

2. Install the required package:
   ```sh
   pip install python-dotenv
   ```

3. Create a `.env` file in the root directory of the project and add your Gmail credentials:
   ```
   GMAIL_USER=your_gmail_address@gmail.com
   GMAIL_PASSWORD=your_gmail_password
   ```

## Usage

1. Run the script from the command line with the recipient's email address and the message as arguments:
   ```sh
   python script.py recipient@example.com "Your message here"
   ```

2. The script will send the email and print "Email sent successfully!" if the email is sent successfully.

## Security Note

For production use, it is recommended to use OAuth2 authentication instead of storing your Gmail password in an environment variable. This script is intended for educational and development purposes only.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This `README.md` provides a clear overview of the script's functionality, installation instructions, usage guidelines, and a security note for handling Gmail credentials securely. It also includes a license section to specify the project's licensing terms.