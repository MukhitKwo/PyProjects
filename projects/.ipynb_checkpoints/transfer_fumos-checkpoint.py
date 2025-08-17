from fileinput import filename
import smtplib
from email.message import EmailMessage
import ssl
from pathlib import Path
import mimetypes
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="config/.env")

sender_email = "mukhitkwo@gmail.com"
app_password = os.getenv("MUK_MAIL_APP_PASSWORD")
receiver_email = "antoniotolstykh@gmail.com"

if app_password is None:
    raise ValueError("MUK_MAIL_APP_PASSWORD environment variable is not set.")

subject = "Fumos"
body = ""

msg = EmailMessage()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.set_content(body)

folder = Path("C:/Users/anton/Desktop")

fumo_files = list(folder.glob("*.jpg")) + list(folder.glob("*.png")) + \
    list(folder.glob("*.gif")) + list(folder.glob("*.mp4"))

for file_path in fumo_files:

    print(file_path)

    mime_type, _ = mimetypes.guess_type(file_path)  # returns the type and extension ("image/jpeg")

    if mime_type:
        maintype, subtype = mime_type.split("/")  # separates the type from extension ("image" and "jpeg")

        with open(file_path, "rb") as f:  # opens the image as a binary
            # adds the binary file to the msg for email
            msg.add_attachment(f.read(), maintype=maintype, subtype=subtype, filename=file_path.name)


context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    print("Sending email...")
    smtp.login(sender_email, app_password)
    smtp.send_message(msg)

print("Email sent with all jpg, png and gif files!")

input("Press Enter...")
