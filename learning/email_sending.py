import smtplib
from email.message import EmailMessage
import ssl
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="config/.env")

sender_email = "mukhitkwo@gmail.com"
app_password = os.getenv("MUK_MAIL_APP_PASSWORD")

if app_password is None:
    raise ValueError("MUK_MAIL_APP_PASSWORD environment variable is not set.")

receiver_email = "antoniotolstykh@gmail.com"

subject = "Hello, I'm from Python"
body = "This is a test"

msg = EmailMessage()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(sender_email, app_password)
    smtp.send_message(msg)

print("Email sent successfully!")
