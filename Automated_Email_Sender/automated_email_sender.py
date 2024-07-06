import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def send_email(to_address, message):
    email = os.getenv("GMAIL_USER")
    password = os.getenv("GMAIL_PASSWORD")

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Automated Email"
    msg["From"] = email
    msg["To"] = to_address

    # Create the body of the message (a plain-text and an HTML version).
    text = message
    html = f"""\
    <html>
      <head></head>
      <body>
        <p>{message}</p>
      </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Attach parts into message container.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, to_address, msg.as_string())
    server.quit()

    print("Email sent successfully!")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <to_address> <message>")
        sys.exit(1)

    to_address = sys.argv[1]
    message = sys.argv[2]

    send_email(to_address, message)
